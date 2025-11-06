"""
Conversation Memory System - GURU AI
Sistem untuk menyimpan dan mengingat konteks percakapan

Features:
- Session management
- Context tracking
- Follow-up question detection
- Topic continuity

Author: GURU AI Enhancement Project
Date: 2025-01-06
"""

import json
import time
from typing import Dict, List, Optional, Any
from pathlib import Path


class ConversationMemory:
    """Manage conversation context and memory"""

    def __init__(self, session_id: str = None):
        """
        Initialize conversation memory

        Args:
            session_id: Unique session identifier
        """
        self.session_id = session_id or f"session_{int(time.time())}"
        self.messages: List[Dict[str, Any]] = []
        self.current_topic: Optional[str] = None
        self.current_subject: Optional[str] = None  # sejarah, fisika, dll
        self.user_level: Optional[str] = None  # sd, smp, sma
        self.user_role: Optional[str] = None  # pelajar, pengajar
        self.metadata: Dict[str, Any] = {}

        # Memory directory
        self.memory_dir = Path(__file__).parent / "memory"
        self.memory_dir.mkdir(exist_ok=True)

    def add_message(self, role: str, content: str, metadata: Optional[Dict] = None):
        """
        Add message to conversation history

        Args:
            role: 'user' or 'assistant'
            content: Message content
            metadata: Additional metadata (topic, subject, etc.)
        """
        message = {
            "role": role,
            "content": content,
            "timestamp": time.time(),
            "metadata": metadata or {}
        }

        self.messages.append(message)

        # Update current topic if provided in metadata
        if metadata:
            if "topic" in metadata:
                self.current_topic = metadata["topic"]
            if "subject" in metadata:
                self.current_subject = metadata["subject"]

    def get_last_user_message(self) -> Optional[str]:
        """Get the last message from user"""
        for msg in reversed(self.messages):
            if msg["role"] == "user":
                return msg["content"]
        return None

    def get_last_assistant_message(self) -> Optional[str]:
        """Get the last message from assistant"""
        for msg in reversed(self.messages):
            if msg["role"] == "assistant":
                return msg["content"]
        return None

    def get_last_topic(self) -> Optional[str]:
        """Get the current or last discussed topic"""
        # Check current topic first
        if self.current_topic:
            return self.current_topic

        # Search in recent messages
        for msg in reversed(self.messages):
            if msg.get("metadata", {}).get("topic"):
                return msg["metadata"]["topic"]

        return None

    def is_followup_question(self, user_input: str) -> bool:
        """
        Detect if user input is a follow-up question

        Args:
            user_input: User's current input

        Returns:
            True if this is a follow-up question
        """
        user_lower = user_input.lower().strip()

        # Check for affirmative responses
        affirmatives = ["ya", "iya", "yoi", "yes", "ok", "okay", "lanjut", "lanjutkan"]
        if user_lower in affirmatives:
            return True

        # Check for follow-up phrases
        followup_phrases = [
            "lebih lanjut",
            "lebih detail",
            "jelaskan lebih",
            "bagaimana dengan",
            "lalu bagaimana",
            "terus",
            "kemudian",
            "selanjutnya"
        ]

        for phrase in followup_phrases:
            if phrase in user_lower:
                return True

        # Check if very short (likely continuation)
        if len(user_lower) < 10 and len(self.messages) > 0:
            # If last message was from assistant and user gives short response
            last_msg = self.get_last_assistant_message()
            if last_msg and len(last_msg) > 100:  # Assistant gave substantial answer
                return True

        return False

    def get_context_summary(self) -> str:
        """
        Get a summary of current conversation context

        Returns:
            Summary string for prompt injection
        """
        if not self.messages:
            return ""

        summary_parts = []

        # Add current topic if exists
        if self.current_topic:
            summary_parts.append(f"Topik yang sedang dibahas: {self.current_topic}")

        # Add recent conversation
        recent_messages = self.messages[-4:]  # Last 2 exchanges
        if recent_messages:
            summary_parts.append("\nPercakapan sebelumnya:")
            for msg in recent_messages:
                role = "User" if msg["role"] == "user" else "Assistant"
                content_preview = msg["content"][:100] + "..." if len(msg["content"]) > 100 else msg["content"]
                summary_parts.append(f"{role}: {content_preview}")

        return "\n".join(summary_parts)

    def get_continuation_prompt(self, user_input: str) -> str:
        """
        Generate continuation prompt when user wants more info

        Args:
            user_input: User's follow-up input

        Returns:
            Prompt for continuing the topic
        """
        topic = self.get_last_topic()

        if not topic:
            # Fallback to analyzing last assistant message
            last_response = self.get_last_assistant_message()
            if last_response:
                return f"User meminta penjelasan lebih lanjut tentang: {last_response[:200]}..."

        # Generate continuation prompt
        if self.is_followup_question(user_input):
            return f"""User mengatakan "{user_input}" sebagai respon terhadap penjelasan sebelumnya tentang {topic}.

User ingin tahu lebih lanjut tentang {topic}. Berikan penjelasan yang lebih mendalam:
- Jelaskan aspek yang belum dijelaskan sebelumnya
- Tambahkan detail dan contoh spesifik
- Diskusikan implikasi atau kontroversi jika ada
- Berikan perspektif yang lebih luas

PENTING: Lanjutkan pembahasan tentang {topic}, BUKAN topik yang berbeda!"""

        return ""

    def save_session(self):
        """Save session to disk"""
        session_file = self.memory_dir / f"{self.session_id}.json"

        data = {
            "session_id": self.session_id,
            "messages": self.messages,
            "current_topic": self.current_topic,
            "current_subject": self.current_subject,
            "user_level": self.user_level,
            "user_role": self.user_role,
            "metadata": self.metadata,
            "created_at": self.messages[0]["timestamp"] if self.messages else time.time(),
            "updated_at": time.time()
        }

        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def load_session(cls, session_id: str) -> 'ConversationMemory':
        """Load session from disk"""
        memory_dir = Path(__file__).parent / "memory"
        session_file = memory_dir / f"{session_id}.json"

        if not session_file.exists():
            return cls(session_id)

        with open(session_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        memory = cls(session_id)
        memory.messages = data.get("messages", [])
        memory.current_topic = data.get("current_topic")
        memory.current_subject = data.get("current_subject")
        memory.user_level = data.get("user_level")
        memory.user_role = data.get("user_role")
        memory.metadata = data.get("metadata", {})

        return memory

    def clear(self):
        """Clear conversation history"""
        self.messages = []
        self.current_topic = None
        self.current_subject = None

    def extract_topic_from_query(self, query: str) -> Optional[str]:
        """
        Extract topic from user query

        Args:
            query: User's question

        Returns:
            Extracted topic or None
        """
        query_lower = query.lower()

        # Historical figures
        figures = [
            "soeharto", "soekarno", "hatta", "sudirman", "diponegoro",
            "cut nyak dien", "ki hajar dewantara"
        ]
        for figure in figures:
            if figure in query_lower:
                return figure.title()

        # Historical events
        events = [
            "g30s", "pki", "proklamasi", "perang jawa", "perang diponegoro",
            "pahlawan revolusi", "pahlawan nasional", "orde baru", "reformasi"
        ]
        for event in events:
            if event in query_lower:
                return event.title()

        # Science topics
        science_topics = [
            "fotosintesis", "newton", "gravitasi", "elektromagnet",
            "faraday", "termodinamika"
        ]
        for topic in science_topics:
            if topic in query_lower:
                return topic.title()

        return None


# Global session management
_active_sessions: Dict[str, ConversationMemory] = {}


def get_or_create_session(session_id: str = "default") -> ConversationMemory:
    """
    Get or create a conversation session

    Args:
        session_id: Session identifier

    Returns:
        ConversationMemory instance
    """
    if session_id not in _active_sessions:
        _active_sessions[session_id] = ConversationMemory.load_session(session_id)

    return _active_sessions[session_id]


def save_all_sessions():
    """Save all active sessions"""
    for memory in _active_sessions.values():
        memory.save_session()
