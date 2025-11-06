# 📚 MCP Education Server - Complete Design & Implementation Guide

**Project:** GURU AI Education MCP Server
**Date:** 2025-01-06
**Purpose:** MCP server untuk menyediakan materi pendidikan terverifikasi dari Kemendikbud

---

## 🎯 Vision

**Goal:** Membuat **MCP (Model Context Protocol) Server** yang menyediakan:
- ✅ Materi pendidikan resmi dari Kemendikbud
- ✅ Library pustaka (buku teks, modul)
- ✅ Fakta-fakta terverifikasi (sejarah, sains, matematika)
- ✅ Conversation memory untuk konteks berkelanjutan
- ✅ Multi-subject support (Sejarah, Fisika, Kimia, Biologi, Matematika, dll)

**Benefits:**
- AI akan selalu menggunakan sumber resmi & terverifikasi
- Konsisten dengan kurikulum nasional
- Zero hallucination untuk materi yang ada di MCP
- Conversation context awareness

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    GURU AI Application                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  1. User Query: "Siapa Soeharto?"                       │    │
│  └────────────────┬───────────────────────────────────────┘    │
│                   │                                             │
│                   ▼                                             │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  2. Memory Check: Load conversation context            │    │
│  │     - Previous topic: None                              │    │
│  │     - User preferences: SMA level                       │    │
│  └────────────────┬───────────────────────────────────────┘    │
│                   │                                             │
│                   ▼                                             │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  3. MCP Query: Request "Soeharto" from Education MCP   │    │
│  └────────────────┬───────────────────────────────────────┘    │
│                   │                                             │
└───────────────────┼─────────────────────────────────────────────┘
                    │
                    │ MCP Protocol (JSON-RPC)
                    │
┌───────────────────▼─────────────────────────────────────────────┐
│              Education MCP Server                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  4. Resource Lookup                                     │    │
│  │     - Check: education://sejarah/tokoh/soeharto        │    │
│  │     - Source: Kemendikbud verified database            │    │
│  └────────────────┬───────────────────────────────────────┘    │
│                   │                                             │
│                   ▼                                             │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  5. Return Verified Facts                               │    │
│  │     {                                                   │    │
│  │       "name": "Soeharto",                               │    │
│  │       "birth": "1921-06-08",                            │    │
│  │       "role": "Presiden RI ke-2",                       │    │
│  │       "period": "1967-1998",                            │    │
│  │       "facts": [...verified data...],                   │    │
│  │       "sources": ["Kemendikbud", "BPNB"]               │    │
│  │     }                                                   │    │
│  └────────────────┬───────────────────────────────────────┘    │
│                   │                                             │
└───────────────────┼─────────────────────────────────────────────┘
                    │
                    │ Return to App
                    │
┌───────────────────▼─────────────────────────────────────────────┐
│              GURU AI Application                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  6. Save to Memory                                      │    │
│  │     - Current topic: "Soeharto"                         │    │
│  │     - Context: "Discussing Orde Baru era"               │    │
│  │     - Last question: "Siapa Soeharto?"                  │    │
│  └────────────────┬───────────────────────────────────────┘    │
│                   │                                             │
│                   ▼                                             │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  7. Generate Response with Context                      │    │
│  │     - Use MCP facts                                     │    │
│  │     - Maintain conversation flow                        │    │
│  │     - Reference previous topics                         │    │
│  └────────────────┬───────────────────────────────────────┘    │
│                   │                                             │
│                   ▼                                             │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  User: "ya" (wants more info)                           │    │
│  └────────────────┬───────────────────────────────────────┘    │
│                   │                                             │
│                   ▼                                             │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  8. Memory Check: Load context                          │    │
│  │     ✅ Previous topic: "Soeharto"                        │    │
│  │     ✅ User said "ya" = wants continuation              │    │
│  │     ✅ Continue with Soeharto details                    │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 📦 MCP Server Structure

### **Project Directory:**
```
guru-education-mcp/
├── package.json
├── tsconfig.json
├── src/
│   ├── index.ts                    # Main MCP server
│   ├── resources/
│   │   ├── sejarah.ts              # Historical content
│   │   ├── fisika.ts               # Physics content
│   │   ├── kimia.ts                # Chemistry content
│   │   ├── biologi.ts              # Biology content
│   │   ├── matematika.ts           # Mathematics content
│   │   └── index.ts                # Resource registry
│   ├── tools/
│   │   ├── search.ts               # Search across subjects
│   │   ├── quiz.ts                 # Generate quizzes
│   │   └── index.ts                # Tool registry
│   ├── data/
│   │   ├── sejarah/
│   │   │   ├── tokoh/
│   │   │   │   ├── soeharto.json
│   │   │   │   ├── soekarno.json
│   │   │   │   └── ...
│   │   │   ├── peristiwa/
│   │   │   │   ├── g30s-pki.json
│   │   │   │   ├── proklamasi.json
│   │   │   │   └── ...
│   │   │   └── pahlawan/
│   │   │       ├── pahlawan-revolusi.json
│   │   │       └── pahlawan-nasional.json
│   │   ├── fisika/
│   │   │   ├── mekanika/
│   │   │   ├── termodinamika/
│   │   │   └── ...
│   │   └── ...
│   └── types/
│       └── index.ts                # TypeScript types
└── README.md
```

---

## 💻 Implementation

### **1. package.json**

```json
{
  "name": "guru-education-mcp",
  "version": "1.0.0",
  "description": "MCP server for verified Indonesian educational content",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "ts-node src/index.ts"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.5.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "typescript": "^5.0.0",
    "ts-node": "^10.9.0"
  },
  "keywords": ["mcp", "education", "indonesia", "kemendikbud"],
  "author": "GURU AI Project",
  "license": "MIT"
}
```

---

### **2. src/data/sejarah/tokoh/soeharto.json**

```json
{
  "id": "soeharto",
  "name": "Soeharto",
  "fullName": "Soeharto",
  "birth": {
    "date": "1921-06-08",
    "place": "Kemusuk, Argomulyo, Yogyakarta"
  },
  "death": {
    "date": "2008-01-27",
    "place": "Jakarta"
  },
  "roles": [
    "Presiden Republik Indonesia ke-2 (1967-1998)",
    "Panglima Komando Strategis Angkatan Darat (Pangkostrad)",
    "Jenderal TNI"
  ],
  "career": [
    {
      "period": "1940-1942",
      "role": "Tentara KNIL (Koninklijk Nederlandsch-Indisch Leger)"
    },
    {
      "period": "1943-1945",
      "role": "Tentara PETA (Pembela Tanah Air) - Jepang"
    },
    {
      "period": "1945-1949",
      "role": "Tentara Republik Indonesia - Perang Kemerdekaan",
      "note": "Berperang MELAWAN Belanda, BUKAN melawan RI"
    },
    {
      "period": "1965",
      "role": "Pangkostrad - Menumpas G30S/PKI"
    },
    {
      "period": "1966",
      "role": "Penerima Supersemar dari Soekarno"
    },
    {
      "period": "1967-1998",
      "role": "Presiden RI ke-2 - Era Orde Baru"
    }
  ],
  "majorEvents": [
    {
      "year": 1965,
      "event": "Penumpasan G30S/PKI",
      "description": "Memimpin penumpasan kudeta PKI, memulai transisi kekuasaan"
    },
    {
      "year": 1966,
      "event": "Supersemar (Surat Perintah Sebelas Maret)",
      "description": "Menerima mandat dari Soekarno untuk mengambil tindakan keamanan"
    },
    {
      "year": 1967,
      "event": "Pelantikan sebagai Presiden",
      "description": "Dilantik sebagai Pejabat Presiden, kemudian Presiden penuh (1968)"
    },
    {
      "year": 1998,
      "event": "Pengunduran Diri",
      "description": "Mengundurkan diri akibat Reformasi dan krisis moneter 1997-1998"
    }
  ],
  "achievements": [
    "Pembangunan ekonomi pesat (1970-1990an)",
    "Swasembada pangan (1984)",
    "Pembangunan infrastruktur nasional",
    "Stabilitas politik selama 31 tahun"
  ],
  "controversies": [
    "Pelanggaran HAM (Tragedi Trisakti, Semanggi, Tanjung Priok)",
    "Korupsi, Kolusi, dan Nepotisme (KKN)",
    "Pembatasan kebebasan pers dan berpendapat",
    "Sentralisasi kekuasaan"
  ],
  "legacy": {
    "positive": [
      "Pembangunan ekonomi dan infrastruktur",
      "Stabilitas politik jangka panjang",
      "Swasembada pangan"
    ],
    "negative": [
      "Pelanggaran HAM yang sistematis",
      "Korupsi masif",
      "Pembatasan demokrasi"
    ]
  },
  "commonMisconceptions": [
    {
      "wrong": "Soeharto berperang melawan Republik Indonesia",
      "correct": "Soeharto berperang MELAWAN Belanda pada 1945-1949 sebagai tentara RI"
    },
    {
      "wrong": "Soeharto menggulingkan Soekarno dengan kekerasan",
      "correct": "Transisi kekuasaan melalui Supersemar (1966) dan proses politik bertahap"
    }
  ],
  "sources": [
    "Kemendikbud - Buku Sejarah SMA Kelas XII",
    "BPNB (Balai Pelestarian Nilai Budaya)",
    "ANRI (Arsip Nasional Republik Indonesia)"
  ],
  "verifiedDate": "2025-01-06",
  "curriculumRelevance": {
    "level": "SMA",
    "subject": "Sejarah",
    "topics": ["Orde Baru", "Transisi Politik", "Pembangunan Ekonomi"],
    "utbkRelevance": "HIGH"
  }
}
```

---

### **3. src/resources/sejarah.ts**

```typescript
import { Resource } from "@modelcontextprotocol/sdk/types.js";
import * as fs from "fs";
import * as path from "path";

/**
 * Load historical figure data
 */
function loadTokohData(name: string): any {
  const filePath = path.join(__dirname, `../data/sejarah/tokoh/${name}.json`);
  if (fs.existsSync(filePath)) {
    return JSON.parse(fs.readFileSync(filePath, "utf-8"));
  }
  return null;
}

/**
 * Get all historical resources
 */
export function getSejarahResources(): Resource[] {
  const resources: Resource[] = [];

  // List all tokoh files
  const tokohDir = path.join(__dirname, "../data/sejarah/tokoh");
  if (fs.existsSync(tokohDir)) {
    const files = fs.readdirSync(tokohDir);

    files.forEach(file => {
      if (file.endsWith(".json")) {
        const name = file.replace(".json", "");
        resources.push({
          uri: `education://sejarah/tokoh/${name}`,
          name: `Tokoh Sejarah: ${name}`,
          description: `Informasi terverifikasi tentang ${name} dari Kemendikbud`,
          mimeType: "application/json"
        });
      }
    });
  }

  return resources;
}

/**
 * Get specific historical resource content
 */
export function getSejarahResourceContent(uri: string): string | null {
  const match = uri.match(/education:\/\/sejarah\/tokoh\/(.+)/);
  if (match) {
    const name = match[1];
    const data = loadTokohData(name);

    if (data) {
      return JSON.stringify(data, null, 2);
    }
  }

  return null;
}
```

---

### **4. src/index.ts (Main MCP Server)**

```typescript
#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ListToolsRequestSchema,
  CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

import { getSejarahResources, getSejarahResourceContent } from "./resources/sejarah.js";

/**
 * GURU Education MCP Server
 * Provides verified educational content from Indonesian Ministry of Education
 */
class EducationMCPServer {
  private server: Server;

  constructor() {
    this.server = new Server(
      {
        name: "guru-education-mcp",
        version: "1.0.0",
      },
      {
        capabilities: {
          resources: {},
          tools: {},
        },
      }
    );

    this.setupHandlers();
  }

  private setupHandlers() {
    // List all available resources
    this.server.setRequestHandler(ListResourcesRequestSchema, async () => {
      const sejarahResources = getSejarahResources();

      return {
        resources: [
          ...sejarahResources,
          // Add more subjects here
        ],
      };
    });

    // Read specific resource content
    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const uri = request.params.uri;

      // Handle sejarah resources
      if (uri.startsWith("education://sejarah/")) {
        const content = getSejarahResourceContent(uri);
        if (content) {
          return {
            contents: [
              {
                uri,
                mimeType: "application/json",
                text: content,
              },
            ],
          };
        }
      }

      throw new Error(`Resource not found: ${uri}`);
    });

    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [
          {
            name: "search_education_content",
            description: "Search across all educational content by keywords",
            inputSchema: {
              type: "object",
              properties: {
                query: {
                  type: "string",
                  description: "Search query (e.g., 'Soeharto', 'pahlawan revolusi')",
                },
                subject: {
                  type: "string",
                  enum: ["sejarah", "fisika", "kimia", "biologi", "matematika", "all"],
                  description: "Subject to search in (default: all)",
                },
              },
              required: ["query"],
            },
          },
        ],
      };
    });

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      if (name === "search_education_content") {
        const query = args.query as string;
        const subject = (args.subject as string) || "all";

        // Simple search implementation
        const results: any[] = [];

        if (subject === "all" || subject === "sejarah") {
          // Search in sejarah
          const tokohContent = getSejarahResourceContent(`education://sejarah/tokoh/${query.toLowerCase()}`);
          if (tokohContent) {
            results.push({
              uri: `education://sejarah/tokoh/${query.toLowerCase()}`,
              subject: "sejarah",
              content: tokohContent,
            });
          }
        }

        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(results, null, 2),
            },
          ],
        };
      }

      throw new Error(`Unknown tool: ${name}`);
    });
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error("GURU Education MCP Server running on stdio");
  }
}

// Start the server
const server = new EducationMCPServer();
server.run().catch(console.error);
```

---

## 🔧 Installation & Setup

### **Step 1: Create Project**

```bash
cd /Users/anugrah/Documents/Windsurf/codux/guru
mkdir guru-education-mcp
cd guru-education-mcp

# Initialize npm project
npm init -y

# Install dependencies
npm install @modelcontextprotocol/sdk
npm install --save-dev typescript @types/node ts-node

# Create tsconfig.json
cat > tsconfig.json << 'EOF'
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
EOF
```

### **Step 2: Create Directory Structure**

```bash
mkdir -p src/{resources,tools,data/sejarah/tokoh,types}
```

### **Step 3: Add Content**

Create files as shown above:
- `src/index.ts`
- `src/resources/sejarah.ts`
- `src/data/sejarah/tokoh/soeharto.json`

### **Step 4: Build**

```bash
npm run build
```

### **Step 5: Configure in Claude Code**

Add to Claude Code MCP config (`~/.config/claude-code/mcp_settings.json`):

```json
{
  "mcpServers": {
    "guru-education": {
      "command": "node",
      "args": ["/Users/anugrah/Documents/Windsurf/codux/guru/guru-education-mcp/dist/index.js"],
      "env": {}
    }
  }
}
```

---

## 🧪 Testing

### **Test 1: List Resources**

```typescript
// In Claude Code, MCP should show:
mcp__guru-education__list_resources()

// Returns:
[
  {
    "uri": "education://sejarah/tokoh/soeharto",
    "name": "Tokoh Sejarah: soeharto",
    "description": "Informasi terverifikasi tentang soeharto dari Kemendikbud"
  }
]
```

### **Test 2: Read Resource**

```typescript
mcp__guru-education__read_resource({
  uri: "education://sejarah/tokoh/soeharto"
})

// Returns: Full JSON data about Soeharto
```

### **Test 3: Search**

```typescript
mcp__guru-education__search_education_content({
  query: "soeharto",
  subject: "sejarah"
})

// Returns: Matching content
```

---

## 📊 Benefits

### **With MCP Server:**

**BEFORE (Local RAG only):**
```
❌ Limited to what we manually add to historical_facts_db.py
❌ Hard to update (need code changes)
❌ No central authority
❌ Python-only
```

**AFTER (MCP Server):**
```
✅ Central source of truth (Kemendikbud data)
✅ Easy to update (just edit JSON files)
✅ Reusable across applications
✅ Language-agnostic (any MCP client can use)
✅ Scalable (add subjects easily)
✅ Version controlled
```

---

## 🎯 Next Steps

1. **Expand Content:**
   - Add more tokoh (Soekarno, Hatta, dll)
   - Add peristiwa (Proklamasi, dll)
   - Add other subjects (Fisika, Kimia, dll)

2. **Enhance Features:**
   - Full-text search
   - Quiz generation
   - Related content suggestions

3. **Integration:**
   - Connect GURU AI to MCP
   - Add conversation memory
   - Implement context awareness

---

**See Next Document:** `CONVERSATION_MEMORY_DESIGN.md` for memory implementation
**See Next Document:** `MCP_INTEGRATION_TUTORIAL.md` for integration guide
