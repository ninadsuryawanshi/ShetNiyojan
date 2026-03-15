# ShetNiyojan – Detailed Project Documentation

<div align="center">
  <img src="Frontend/src/assets/logo.png" alt="ShetNiyojan Logo" width="120">
  <h3>Comprehensive Agricultural Management Platform</h3>
</div>

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [System Architecture](#2-system-architecture)
3. [Technology Stack](#3-technology-stack)
4. [Project Structure](#4-project-structure)
5. [Frontend Implementation](#5-frontend-implementation)
   - 5.1 [Application Entry Point](#51-application-entry-point)
   - 5.2 [Routing](#52-routing)
   - 5.3 [Authentication Context](#53-authentication-context)
   - 5.4 [Multilingual Support](#54-multilingual-support)
   - 5.5 [API Client](#55-api-client)
   - 5.6 [Pages](#56-pages)
   - 5.7 [Feature Components](#57-feature-components)
   - 5.8 [Dashboard Components](#58-dashboard-components)
   - 5.9 [UI Component Library](#59-ui-component-library)
6. [Backend Implementation](#6-backend-implementation)
   - 6.1 [Application Bootstrap](#61-application-bootstrap)
   - 6.2 [Database Layer](#62-database-layer)
   - 6.3 [Authentication & Middleware](#63-authentication--middleware)
   - 6.4 [User Management APIs](#64-user-management-apis)
   - 6.5 [Yield Management APIs](#65-yield-management-apis)
   - 6.6 [Activity Tracking APIs](#66-activity-tracking-apis)
   - 6.7 [AI/ML Feature APIs](#67-aiml-feature-apis)
   - 6.8 [Supply Chain & Transport APIs](#68-supply-chain--transport-apis)
   - 6.9 [Lease Marketplace APIs](#69-lease-marketplace-apis)
   - 6.10 [Chatbot API](#610-chatbot-api)
7. [Machine Learning Models](#7-machine-learning-models)
   - 7.1 [Plant Disease Detection](#71-plant-disease-detection)
   - 7.2 [Crop Recommendation](#72-crop-recommendation)
   - 7.3 [Fertilizer Prediction](#73-fertilizer-prediction)
   - 7.4 [Soil Analysis](#74-soil-analysis)
8. [Database Schema](#8-database-schema)
9. [API Reference](#9-api-reference)
10. [Data Flow Diagrams](#10-data-flow-diagrams)
11. [External Integrations](#11-external-integrations)
12. [Configuration & Environment Variables](#12-configuration--environment-variables)
13. [Installation & Setup](#13-installation--setup)
14. [Available Scripts](#14-available-scripts)
15. [Security Considerations](#15-security-considerations)
16. [Deployment Guide](#16-deployment-guide)
17. [Future Enhancements](#17-future-enhancements)
18. [Contributors](#18-contributors)

---

## 1. Project Overview

**ShetNiyojan** (शेत नियोजन, meaning *Farm Planning* in Marathi) is a full-stack agricultural management platform designed to empower Indian farmers with data-driven insights. It combines modern web technologies with machine learning models and large language models (LLMs) to guide farmers through every stage of the agricultural lifecycle.

### Core Problem Being Solved

Indian farmers often lack access to structured decision-making tools for:
- Choosing the right crop for their specific soil and climate conditions.
- Identifying and treating plant diseases early.
- Maximising profit by optimising the route and destination for selling produce.
- Tracking farm expenses and activities in a structured way.
- Renting/leasing farming equipment affordably.

ShetNiyojan addresses all of these use cases in a single, mobile-friendly platform.

### Agricultural Lifecycle Coverage

| Phase | Features |
|-------|---------|
| **Phase 1 – Planning & Preparation** | AI crop recommendation, Equipment lease marketplace |
| **Phase 2 – Growing & Monitoring** | Plant disease detection, Treatment recommendations, Activity tracking |
| **Phase 3 – Harvest & Distribution** | Supply chain optimisation, Market price analysis, Transport route planning |

---

## 2. System Architecture

ShetNiyojan uses a classic **client–server** architecture with a separate React frontend and a Python/Flask backend.

```
┌─────────────────────────────────────────────────────────────┐
│                       CLIENT (Browser)                      │
│                                                             │
│  React 18 + TypeScript + Vite + Tailwind CSS + Shadcn UI   │
│                                                             │
│  ┌─────────────┐  ┌────────────┐  ┌───────────────────┐    │
│  │  Auth Layer │  │  Routing   │  │  State / Context  │    │
│  └─────────────┘  └────────────┘  └───────────────────┘    │
│                          │                                  │
│                   Axios HTTP Client                         │
└──────────────────────────┼──────────────────────────────────┘
                           │  REST API  (JSON over HTTP)
                           │  x-access-token header
┌──────────────────────────┼──────────────────────────────────┐
│                    SERVER (Flask)                           │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  Flask Application                  │   │
│  │  CORS enabled for /api/*                            │   │
│  │  Token middleware (@token_required)                 │   │
│  └──────────────────────────┬──────────────────────────┘   │
│                             │                               │
│  ┌──────────┐  ┌─────────┐  │  ┌────────┐  ┌───────────┐  │
│  │  Auth    │  │ Yields  │  │  │  ML    │  │  Supply   │  │
│  │  Routes  │  │ Routes  │  │  │  APIs  │  │  Chain    │  │
│  └──────────┘  └─────────┘  │  └────────┘  └───────────┘  │
│                             │                               │
│  ┌──────────────────────────┴──────────────────────────┐   │
│  │              External Services                      │   │
│  │  Groq LLM  │  Google GenAI  │  Mandi API            │   │
│  │  HuggingFace Models         │  Haversine             │   │
│  └─────────────────────────────────────────────────────┘   │
│                             │                               │
│  ┌──────────────────────────┴──────────────────────────┐   │
│  │                   MongoDB                           │   │
│  │  users │ yields │ activities │ lease_items │ tasks  │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Communication Protocol

- All client-server communication uses **JSON over HTTP**.
- Authentication is handled using a **UUID token** stored in `localStorage` on the client and sent with every protected request as the `x-access-token` header.
- The backend validates the token by looking it up in the `users` collection in MongoDB.

---

## 3. Technology Stack

### Frontend

| Technology | Version | Purpose |
|-----------|---------|---------|
| React | 18.2.0 | UI library |
| TypeScript | ~5.x | Type safety and IDE support |
| Vite | ~5.x | Build tooling and development server |
| Tailwind CSS | 3.4.1 | Utility-first CSS framework |
| Shadcn UI | - | Pre-built accessible component library |
| Radix UI | ~1.x | Headless UI primitives |
| React Router | 6.22.2 | Client-side routing |
| Axios | 1.6.7 | HTTP client |
| React Hook Form | 7.53.0 | Form state management and validation |
| Zod | 3.23.8 | Schema declaration and validation |
| TanStack Query | 5.56.2 | Server-state management and data fetching |
| Recharts | 2.12.7 | Data visualisation charts |
| Lucide React | 0.344.0 | Icon library |
| date-fns | 3.6.0 | Date utility library |
| next-themes | 0.3.0 | Dark/light theme support |
| sonner | 1.4.3 | Toast notifications |

### Backend

| Technology | Version | Purpose |
|-----------|---------|---------|
| Flask | Latest | Python web framework |
| Flask-CORS | Latest | Cross-origin resource sharing |
| PyMongo | Latest | MongoDB driver for Python |
| Werkzeug | Latest | Password hashing utilities |
| bcrypt | Latest | Additional password hashing |
| PyJWT | Latest | JSON Web Token support |
| python-decouple | Latest | Environment variable management |
| Groq SDK | Latest | LLM API client (LLaMA 3) |
| Google Generative AI | Latest | Alternative LLM provider |
| LangChain | Latest | LLM orchestration framework |
| PyTorch | 2.0+ | Deep learning inference |
| Transformers (HF) | 4.36+ | Pre-trained model loading |
| scikit-learn | 1.3+ | ML model utilities |
| XGBoost | Latest | Fertilizer prediction model |
| joblib | Latest | Model serialisation/loading |
| pandas | 2.0+ | Data manipulation |
| numpy | 2.0+ | Numerical computing |
| Pillow | Latest | Image processing |
| haversine | Latest | Geographic distance calculation |
| requests | Latest | HTTP calls to external APIs |

---

## 4. Project Structure

```
ShetNiyojan/
│
├── Backend/                          # Python/Flask backend
│   ├── app.py                        # Main Flask application (2,068+ lines)
│   ├── db.py                         # MongoDB connection & collections
│   ├── plant_disease_model.py        # MobileNetV2 disease classifier
│   ├── requirements.txt              # Python dependencies
│   ├── models/                       # Serialised ML model files
│   │   ├── crop_recommendation/      # Crop recommendation artefacts
│   │   ├── xgb_fertilizer_model.pkl  # XGBoost fertilizer model
│   │   ├── adaboost_model_soil.pkl   # AdaBoost soil analysis model
│   │   └── (label encoders, scalers)
│   ├── datasets/
│   │   └── fertilizer.csv            # Fertilizer training dataset
│   ├── scripts/                      # Jupyter notebooks & helper scripts
│   └── uploads/                      # Temporary image uploads
│
├── Frontend/                         # React/TypeScript frontend
│   ├── src/
│   │   ├── main.tsx                  # Application entry point
│   │   ├── App.tsx                   # Root component with routing
│   │   ├── vite-env.d.ts             # Vite environment type declarations
│   │   │
│   │   ├── pages/                    # Full-page route components
│   │   │   ├── Index.tsx             # Landing/home page
│   │   │   ├── Login.tsx             # Login page
│   │   │   ├── Register.tsx          # Registration page
│   │   │   ├── Dashboard.tsx         # Main user dashboard
│   │   │   ├── YieldDetails.tsx      # Individual yield detail view
│   │   │   ├── LeaseMarketPlace.tsx  # Equipment marketplace
│   │   │   └── NotFound.tsx          # 404 error page
│   │   │
│   │   ├── components/
│   │   │   ├── common/               # Shared layout components
│   │   │   │   ├── DashboardHeader.tsx
│   │   │   │   └── LanguageSelector.tsx
│   │   │   ├── dashboard/            # Dashboard sub-components
│   │   │   │   ├── ActivityLog.tsx
│   │   │   │   ├── CurrentYields.tsx
│   │   │   │   ├── DashboardSidebar.tsx
│   │   │   │   ├── WeatherInfo.tsx
│   │   │   │   └── YieldModal.tsx
│   │   │   ├── ui/                   # Shadcn UI component library (45+)
│   │   │   ├── CropPrediction.tsx    # AI crop recommendation UI
│   │   │   ├── CropHealthMonitoring.tsx  # Disease detection UI
│   │   │   ├── SupplyChain.tsx       # Supply chain optimisation UI
│   │   │   ├── ChatBot.tsx           # AI chatbot UI
│   │   │   ├── Marketplace.tsx       # Marketplace UI
│   │   │   ├── Hero.tsx              # Landing page hero section
│   │   │   └── Features.tsx          # Landing page features section
│   │   │
│   │   ├── hooks/                    # Custom React hooks
│   │   │   ├── use-toast.ts          # Toast notification hook
│   │   │   └── use-mobile.tsx        # Mobile device detection hook
│   │   │
│   │   ├── layouts/
│   │   │   └── MainLayout.tsx        # Common page layout wrapper
│   │   │
│   │   ├── lib/
│   │   │   ├── api.ts                # Axios API client with interceptors
│   │   │   ├── auth-context.tsx      # Global authentication state
│   │   │   ├── translator-context.tsx # i18n / multilingual support
│   │   │   └── utils.ts              # Utility functions
│   │   │
│   │   └── assets/                   # Static images, icons, logo
│   │
│   ├── public/                       # Public static files
│   ├── package.json                  # npm dependencies
│   ├── tsconfig.json                 # TypeScript configuration
│   ├── vite.config.ts                # Vite build configuration
│   ├── tailwind.config.ts            # Tailwind CSS configuration
│   ├── eslint.config.js              # ESLint rules
│   └── postcss.config.js             # PostCSS configuration
│
├── README.md                         # Project overview
├── DOCUMENTATION.md                  # This file
└── .gitignore
```

---

## 5. Frontend Implementation

### 5.1 Application Entry Point

**File:** `Frontend/src/main.tsx`

The entry point renders the root `<App />` component inside `React.StrictMode`. It wraps the entire app with providers:
- `BrowserRouter` – enables client-side routing.
- `AuthProvider` – supplies global authentication state.
- `TranslatorProvider` – supplies the current language and translation function.
- `QueryClientProvider` – enables TanStack Query for server-state management.
- `Toaster` – renders global toast notifications.

### 5.2 Routing

**File:** `Frontend/src/App.tsx`

Routing is implemented using **React Router v6**. The route table is:

| Path | Component | Protected |
|------|-----------|-----------|
| `/` | `Index` (Landing Page) | No |
| `/login` | `Login` | No |
| `/register` | `Register` | No |
| `/dashboard` | `Dashboard` | Yes |
| `/yields/:yieldId` | `YieldDetails` | Yes |
| `/lease-marketplace` | `LeaseMarketPlace` | Yes |
| `*` | `NotFound` | No |

Protected routes check for the presence of an authentication token; unauthenticated users are redirected to `/login`.

### 5.3 Authentication Context

**File:** `Frontend/src/lib/auth-context.tsx`

Implements React Context to provide a global authentication state. The context exposes:

```typescript
interface AuthContextType {
  user: User | null;
  token: string | null;
  login: (token: string, userData: User) => void;
  logout: () => void;
  isAuthenticated: boolean;
}
```

- On login, the token and user details are stored in `localStorage` and updated in context.
- On logout, `localStorage` is cleared and the user is redirected to `/login`.
- On app load, the token is read from `localStorage` to restore the session.

### 5.4 Multilingual Support

**File:** `Frontend/src/lib/translator-context.tsx`

Provides a translation context using React Context and a simple key-value string map. It supports:
- Language switching (English, Marathi, Hindi).
- A `translate(key: string)` function available to all components via the `useTranslator` hook.
- Language preference is persisted in `localStorage`.

### 5.5 API Client

**File:** `Frontend/src/lib/api.ts`

A pre-configured **Axios** instance with:

```typescript
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:5000/api',
});

// Request interceptor - attaches x-access-token header
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers['x-access-token'] = token;
  }
  return config;
});
```

All API calls across the application use this single instance to ensure consistent authentication token injection.

### 5.6 Pages

#### Landing Page (`Index.tsx`)
The public landing page composed of:
- `Hero` – headline, call-to-action, and platform benefits.
- `Features` – carousel/grid of key platform features.
- Navigation links to `Login` and `Register`.

#### Login (`Login.tsx`)
- Form with mobile number and password fields.
- Calls `POST /api/users/login`.
- On success, stores the token via `AuthContext.login()` and navigates to `/dashboard`.
- Uses React Hook Form with Zod validation.

#### Register (`Register.tsx`)
- Form with full name, mobile number, and password fields.
- Calls `POST /api/users/register`.
- On success, redirects to `/login`.
- Uses React Hook Form with Zod validation.

#### Dashboard (`Dashboard.tsx`)
The authenticated home screen. Displays:
- Welcome message and user profile.
- Summary cards for active yields.
- Recent activity timeline.
- Navigation panels to all features (Crop Prediction, Health Monitoring, Supply Chain, Chatbot).
- Modals for creating new yields.

#### YieldDetails (`YieldDetails.tsx`)
A detailed view for an individual yield, showing:
- Yield metadata (name, acres, status, creation date).
- Activity timeline with filters.
- Status update controls.
- Link to run crop health analysis.
- Charts for expense tracking.

#### Lease Marketplace (`LeaseMarketPlace.tsx`)
- Displays paginated listings of available equipment for rent.
- Supports filtering by category and search.
- Authenticated users can list their own equipment.
- CRUD operations for lease items.

### 5.7 Feature Components

#### Crop Prediction (`CropPrediction.tsx`)

Collects soil and climate parameters from the user via a form:
- N (Nitrogen content)
- P (Phosphorus content)
- K (Potassium content)
- Temperature (°C)
- Humidity (%)
- pH
- Rainfall (mm)
- Location (free text)

Sends these parameters to `POST /api/crop-recommendation` and renders the structured JSON response containing:
- Best recommended crop
- Alternative crops
- Farming practice recommendations
- Estimated yield
- Environmental suitability rating
- Additional crop comparison table

#### Crop Health Monitoring (`CropHealthMonitoring.tsx`)

Allows farmers to upload a photo of an affected plant for AI-powered disease diagnosis:
1. User selects or captures an image.
2. Image is sent via multipart form data to `POST /api/plant-disease-analysis`.
3. Backend runs MobileNetV2 inference to identify the disease class.
4. Groq LLaMA 3 generates a detailed JSON report covering:
   - Disease name and scientific description
   - Causes and conditions
   - Visual symptoms
   - Treatment recommendations
   - Pesticide/fertilizer doses and frequency
5. The frontend renders this information in a structured card layout.

#### Supply Chain (`SupplyChain.tsx`)

Helps farmers maximise revenue by optimising where to sell their crop:
1. User inputs: origin city, crop type, and crop weight (kg).
2. Sends to `POST /api/optimize-transport`.
3. Backend queries the Mandi API for real-time commodity prices and calculates transport costs using the Haversine formula.
4. Returns profit analysis for all destination cities.
5. The frontend renders:
   - A summary card showing the best destination city.
   - A table comparing prices, transport costs, and net profit per destination.
   - An embedded map rendered by the backend using Leaflet.js.

#### Chatbot (`ChatBot.tsx`)

A real-time conversational AI assistant:
- Input field for typing questions.
- Messages sent to `POST /api/chat`.
- Backend uses Groq LLaMA 3 70B to generate concise agricultural guidance formatted in HTML.
- Responses are rendered as HTML inside message bubbles.
- Chat history is maintained in component state for the current session.

### 5.8 Dashboard Components

| Component | Description |
|-----------|-------------|
| `DashboardHeader` | Top navigation bar with search and user menu |
| `DashboardSidebar` | Left-side feature navigation with collapsible menu |
| `ActivityLog` | Timeline of recent farm activities |
| `CurrentYields` | Grid of active yield cards with status badges |
| `YieldModal` | Modal form for creating a new yield |
| `WeatherInfo` | Weather widget (placeholder for future integration) |
| `LanguageSelector` | Dropdown to switch app language |

### 5.9 UI Component Library

Located in `Frontend/src/components/ui/`, this folder contains 45+ Shadcn UI components built on Radix UI primitives and styled with Tailwind CSS. Key components include:

`button`, `card`, `dialog`, `dropdown-menu`, `form`, `input`, `label`, `select`, `sheet`, `skeleton`, `table`, `tabs`, `textarea`, `toast`, `tooltip`, `badge`, `calendar`, `checkbox`, `popover`, `progress`, `radio-group`, `scroll-area`, `separator`, `slider`, `switch`, `accordion`, `alert`, `avatar`, `breadcrumb`, `collapsible`, `command`, `context-menu`, `drawer`, `hover-card`, `menubar`, `navigation-menu`, `pagination`, `resizable`, `sidebar`, `sonner`, `toggle`, `toggle-group`.

All components follow the same composable API pattern, accepting `className` for Tailwind overrides and `ref` forwarding.

---

## 6. Backend Implementation

### 6.1 Application Bootstrap

**File:** `Backend/app.py`

```python
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

- Flask app is created and CORS is enabled for all `/api/*` routes, allowing the React frontend to call the API from any origin.
- A `transport_logger` is configured for structured logging of transport optimisation operations.
- Mandi API credentials and city coordinate data are configured as module-level constants.

### 6.2 Database Layer

**File:** `Backend/db.py`

MongoDB is used as the primary data store. The connection is established using **PyMongo**:

```python
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client['shetniyojan']
```

If MongoDB is unavailable (e.g., during development without a local MongoDB instance), the module falls back to a **FakeDB** implementation that stubs all operations, allowing the rest of the application to start.

Collections initialised:
- `users_collection = db['users']`
- `tasks_collection = db['tasks']`
- `yields_collection = db['yields']`
- `activities_collection = db['activities']`
- `db['lease_items']` (index created on `name`)

### 6.3 Authentication & Middleware

**File:** `Backend/app.py` (lines 68–104)

Authentication is implemented as a Python decorator using `functools.wraps`:

```python
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
        user = users_collection.find_one({"token": token})
        if not user:
            # Development fallback – creates an in-memory test user
            ...
        return f(user, *args, **kwargs)
    return decorated
```

Any route decorated with `@token_required` receives the resolved `current_user` document as its first argument.

**Password Hashing:** User passwords are hashed with Werkzeug's `generate_password_hash()` (PBKDF2-HMAC-SHA256) before storage. Login verification uses `check_password_hash()`.

**Token Generation:** On successful login, a UUID4 string is generated and stored in the user's MongoDB document. This token acts as a session identifier.

### 6.4 User Management APIs

#### Register

```
POST /api/users/register
Content-Type: application/json

{
  "fullname": "Ninad Suryawanshi",
  "mobileno": "9876543210",
  "password": "securepassword"
}
```

- Validates all fields are present.
- Checks for existing user with the same mobile number.
- Hashes the password.
- Inserts a new user document with `token: null`.
- Returns `201 Created` on success.

#### Login

```
POST /api/users/login
Content-Type: application/json

{
  "mobileno": "9876543210",
  "password": "securepassword"
}
```

- Validates fields.
- Fetches user by mobile number.
- Verifies the password hash.
- Generates a new UUID token.
- Updates the user document with the new token.
- Returns `{ "token": "<uuid>" }` with `200 OK`.

#### Profile

```
GET /api/users/profile
x-access-token: <token>
```

Returns `{ "fullname": "...", "mobileno": "..." }` for the authenticated user.

### 6.5 Yield Management APIs

Yields represent individual farming plots or crop cycles managed by a user.

#### Document Structure

```json
{
  "_id": "ObjectId",
  "name": "Wheat Field - Block A",
  "acres": 5.0,
  "status": "planning | active | harvested",
  "userId": "ObjectId (reference to users)",
  "createdAt": "ISODate",
  "updatedAt": "ISODate",
  "activityStatus": "mirrors status",
  "type": "optional",
  "description": "optional",
  "daysRemain": "optional",
  "expense": "optional"
}
```

#### Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/api/yields` | Yes | List all yields for the current user |
| `POST` | `/api/yields` | No* | Create a new yield (identified by `mobileno`) |
| `GET` | `/api/yields/<yield_id>` | Yes | Get a specific yield |
| `PUT` | `/api/yields/<yield_id>` | Yes | Update yield status or details |
| `DELETE` | `/api/yields/<yield_id>` | Yes | Delete a yield (with ownership check) |

> *Note: The `POST /api/yields` endpoint uses `mobileno` in the request body instead of the token header for user identification.

### 6.6 Activity Tracking APIs

Activities log specific farm operations (fertiliser application, pesticide spraying, financial transactions, etc.) linked to a yield.

#### Activity Types and Required Fields

| Activity Type | Extra Fields |
|--------------|-------------|
| `fertilizer` | `fertilizer_name`, `quantity`, `bill_image` |
| `pesticide` | `pesticide_name`, `quantity`, `bill_image` |
| `financial` | `financial_category`, `payment_method`, `receipt` |
| (generic) | — |

**Common required fields for all types:** `yield_id`, `mobileno`, `activity_name`, `summary`, `amount`

#### Endpoints

```
POST /api/create_activity
POST /api/activities          ← retrieves activities for a yield
```

The `POST /api/activities` endpoint accepts `{ "mobileno": "...", "yield_id": "..." }` and returns a list of all activities for that yield owned by that user.

### 6.7 AI/ML Feature APIs

#### Plant Disease Analysis

```
POST /api/plant-disease-analysis
Content-Type: multipart/form-data

image: <file>
```

**Implementation Flow:**
1. Receives uploaded image and saves it to `uploads/` directory.
2. Calls `predict_disease(image_path)` from `plant_disease_model.py`.
3. The model returns a predicted class label and confidence score.
4. Constructs a detailed prompt and sends it to the **Groq LLaMA 3.3 70B** model asking for a structured JSON response with disease information.
5. Returns combined response:

```json
{
  "predictedDisease": "Tomato Late Blight",
  "confidence": 94.23,
  "analysis": {
    "diseaseName": "...",
    "description": "...",
    "causes": "...",
    "symptoms": "...",
    "recommendations": "...",
    "doses": "..."
  }
}
```

#### Crop Recommendation

```
POST /api/crop-recommendation
Content-Type: application/json

{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20.5,
  "humidity": 82.0,
  "ph": 6.5,
  "rainfall": 202.9,
  "location": "Pune, Maharashtra"
}
```

**Implementation Flow:**
1. Validates all 8 required fields.
2. Builds a detailed prompt with soil and climate data.
3. Sends to **Groq LLaMA 3.3 70B** requesting a strict JSON response.
4. Extracts JSON from response using regex.
5. Returns parsed JSON:

```json
{
  "bestRecommendedCrop": "Rice",
  "alternativeCrops": ["Maize", "Soybean", "Groundnut"],
  "recommendations": "...",
  "estimatedYield": "4-5 tonnes/hectare",
  "environmentalSuitability": "...",
  "additionalCrops": [
    {
      "crop": "Sugarcane",
      "suitabilityScore": "78",
      "waterRequirement": "high",
      "growthPeriod": "10-12 months"
    }
  ]
}
```

#### Fertilizer Prediction

```
POST /api/predict-fertilizer
Content-Type: application/json

{
  "soil_type": "Sandy",
  "crop_type": "Wheat",
  "N": 80,
  "P": 40,
  "K": 45,
  "temperature": 25,
  "humidity": 60,
  "moisture": 35
}
```

Uses a pre-trained **XGBoost** classifier loaded from `models/xgb_fertilizer_model.pkl`.

### 6.8 Supply Chain & Transport APIs

#### Overview

The supply chain module helps farmers identify the most profitable city to sell their produce by comparing crop prices across markets against transportation costs.

#### Key Internal Functions

**`fetch_crop_prices(crop)`**
- Queries the Mandi API (`https://api.data.gov.in/...`) for real-time commodity prices.
- Falls back to simulated price data if the API is unavailable.
- Maps market-level data to the 5 supported cities.

**`calculate_transport_cost(origin, destination, crop_weight_kg)`**
- Uses the Haversine formula to calculate the great-circle distance between two cities.
- Applies a cost formula:
  ```python
  transport_cost = (distance_km / 5 * fuel_price * 100) + (distance_km * 0.50 * (crop_weight_kg / 100))
  ```

**`TransportOptimizer.optimize_transport(current_city, crop, crop_weight_kg)`**
- Iterates over all destination cities.
- Calculates `net_profit = (price_per_kg × weight) − transport_cost` for each.
- Returns the city with the highest net profit as the recommendation.

#### Endpoints

```
POST /api/optimize-transport
Content-Type: application/json

{
  "current_city": "Mumbai",
  "crop": "Rice",
  "crop_weight_kg": 500
}
```

Response:
```json
{
  "optimization_result": {
    "current_city": "Mumbai",
    "best_city": "Delhi",
    "best_net_profit": 27000.50,
    "recommend_transport": true,
    "city_details": {
      "Mumbai": { "price_per_kg": 52.0, "transport_cost": 0.0, "net_profit": 26000.0 },
      "Delhi":  { "price_per_kg": 57.0, "transport_cost": 1499.50, "net_profit": 27000.50 }
    }
  },
  "available_cities": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"],
  "map_url": "/api/view-map?city=Mumbai&best_city=Delhi&crop=Rice&crop_weight_kg=500"
}
```

```
GET /api/cities          ← Returns city list with lat/lng
GET /api/commodities     ← Returns available commodity list from Mandi API
GET /api/view-map        ← Returns an HTML map page using Leaflet.js
POST /api/cost-reduction-suggestions   ← AI-generated cost reduction advice
```

### 6.9 Lease Marketplace APIs

Full CRUD for equipment lease listings:

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/api/lease-items` | No | List all lease items |
| `POST` | `/api/lease-items` | Yes | Create a new lease listing |
| `GET` | `/api/lease-items/<item_id>` | No | Get a specific item |
| `PUT` | `/api/lease-items/<item_id>` | Yes | Update a listing |
| `DELETE` | `/api/lease-items/<item_id>` | Yes | Delete a listing |
| `GET` | `/api/lease-items/categories` | No | Get available categories |

#### Lease Item Schema

```json
{
  "_id": "ObjectId",
  "name": "Tractor - 45HP",
  "category": "Tractors",
  "price": 1500,
  "priceUnit": "per day",
  "availability": true,
  "description": "...",
  "ownerId": "ObjectId",
  "createdAt": "ISODate"
}
```

### 6.10 Chatbot API

```
POST /api/chat
Content-Type: application/json

{
  "message": "What is the best time to sow wheat in Maharashtra?",
  "model": "llama-3.3-70b-versatile",
  "temperature": 0.7,
  "max_tokens": 400
}
```

- Sends the message to **Groq LLaMA 3.3 70B** with a system prompt instructing it to act as a concise agricultural assistant.
- Responses are formatted with basic HTML tags (`<p>`, `<ul>`, `<li>`, `<strong>`, `<h3>`) for readability in the chat UI.
- Returns `{ "response": "<html content>" }`.

---

## 7. Machine Learning Models

### 7.1 Plant Disease Detection

**File:** `Backend/plant_disease_model.py`

**Model:** `linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification` (Hugging Face Hub)

**Architecture:** MobileNetV2 – a lightweight convolutional neural network optimised for mobile and embedded vision applications.

**Implementation:**

```python
processor = AutoImageProcessor.from_pretrained("linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")
model = AutoModelForImageClassification.from_pretrained("linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification")

def predict_disease(image_path: str):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_class = model.config.id2label[predicted_class_idx]
    return {
        "class": predicted_class,
        "confidence": torch.softmax(logits, dim=1)[0][predicted_class_idx].item()
    }
```

- The model and processor are **loaded once at module import** time to avoid repeated disk I/O on every request.
- Inference runs in a `torch.no_grad()` context for memory efficiency.
- The predicted class label is mapped back using `model.config.id2label`.

### 7.2 Crop Recommendation

The crop recommendation feature does **not** use a locally trained classifier for the final output. Instead, it uses the **Groq LLaMA 3.3 70B** language model with a structured prompt containing the soil and climate parameters. The pre-trained model artifacts in `models/crop_recommendation/` may be used for supplementary pre-processing or validation steps.

### 7.3 Fertilizer Prediction

**Model File:** `Backend/models/xgb_fertilizer_model.pkl`

An **XGBoost** gradient-boosted tree classifier trained to predict the appropriate fertilizer type given:
- Soil type (categorical, label-encoded)
- Crop type (categorical, label-encoded)
- Nitrogen (N), Phosphorus (P), Potassium (K) levels
- Temperature, Humidity, and Moisture readings

The model is loaded with `joblib.load()` at request time. Input features are pre-processed using stored encoders and scalers before inference.

### 7.4 Soil Analysis

**Model File:** `Backend/models/adaboost_model_soil.pkl`

An **AdaBoost** ensemble classifier for soil health classification. Used to categorise soil into quality tiers which feed into crop and fertilizer recommendations.

---

## 8. Database Schema

### Collection: `users`

| Field | Type | Description |
|-------|------|-------------|
| `_id` | ObjectId | Primary key (MongoDB auto-generated) |
| `fullname` | String | User's full name |
| `mobileno` | String | Mobile number (unique, used as login identifier) |
| `password` | String | Bcrypt/PBKDF2 hashed password |
| `token` | String / null | Active session token (UUID4), set on login |

### Collection: `yields`

| Field | Type | Description |
|-------|------|-------------|
| `_id` | ObjectId | Primary key |
| `name` | String | Name of the yield/plot |
| `acres` | Float | Size of the plot in acres |
| `status` | String | `planning`, `active`, or `harvested` |
| `activityStatus` | String | Mirrors `status` |
| `userId` | ObjectId | Reference to `users._id` |
| `createdAt` | DateTime | Creation timestamp |
| `updatedAt` | DateTime | Last update timestamp |
| `type` | String | Optional crop type |
| `description` | String | Optional description |
| `daysRemain` | Number | Optional days remaining |
| `expense` | Number | Optional tracked expense |

### Collection: `activities`

| Field | Type | Description |
|-------|------|-------------|
| `_id` | ObjectId | Primary key |
| `userId` | ObjectId | Reference to `users._id` |
| `yieldId` | ObjectId | Reference to `yields._id` |
| `activity_type` | String | `fertilizer`, `pesticide`, `financial`, or generic |
| `activity_name` | String | Short activity name |
| `summary` | String | Description of the activity |
| `amount` | Number | Cost/amount associated |
| `created_at` | DateTime | UTC creation timestamp |
| `fertilizer_name` | String | (fertilizer only) |
| `pesticide_name` | String | (pesticide only) |
| `quantity` | Number | (fertilizer/pesticide only) |
| `bill_image` | String | (fertilizer/pesticide only) Base64 or file path |
| `financial_category` | String | (financial only) |
| `payment_method` | String | (financial only) |
| `receipt` | String | (financial only) |

### Collection: `lease_items`

| Field | Type | Description |
|-------|------|-------------|
| `_id` | ObjectId | Primary key |
| `name` | String | Equipment name (indexed) |
| `category` | String | Equipment category |
| `price` | Number | Rental price |
| `priceUnit` | String | Price unit (e.g., "per day") |
| `availability` | Boolean | Whether currently available |
| `description` | String | Optional description |
| `ownerId` | ObjectId | Reference to `users._id` |
| `createdAt` | DateTime | Creation timestamp |

### Collection: `tasks`

Initialised but reserved for future task management features.

---

## 9. API Reference

### Base URL

```
http://localhost:5000/api
```

### Authentication

All protected endpoints require:
```
x-access-token: <uuid-token>
```

### Full Endpoint Summary

| Method | Endpoint | Auth Required | Summary |
|--------|----------|---------------|---------|
| `POST` | `/users/register` | No | Register new user |
| `POST` | `/users/login` | No | Login and receive token |
| `GET` | `/users/profile` | Yes | Get current user profile |
| `GET` | `/yields` | Yes | List user's yields |
| `POST` | `/yields` | No* | Create a yield |
| `GET` | `/yields/<id>` | Yes | Get yield details |
| `PUT` | `/yields/<id>` | Yes | Update yield |
| `DELETE` | `/yields/<id>` | Yes | Delete yield |
| `POST` | `/create_activity` | No* | Create a farm activity |
| `POST` | `/activities` | No* | Get activities for a yield |
| `POST` | `/plant-disease-analysis` | No | Analyse plant disease image |
| `POST` | `/crop-recommendation` | No | Get AI crop recommendation |
| `POST` | `/predict-fertilizer` | No | Get fertilizer recommendation |
| `POST` | `/optimize-transport` | No | Optimise transport route |
| `GET` | `/cities` | No | Get available cities |
| `GET` | `/commodities` | No | Get commodity list |
| `GET` | `/view-map` | No | Get map HTML |
| `POST` | `/cost-reduction-suggestions` | No | Get cost reduction advice |
| `GET` | `/lease-items` | No | List all lease items |
| `POST` | `/lease-items` | Yes | Create lease item |
| `GET` | `/lease-items/<id>` | No | Get lease item |
| `PUT` | `/lease-items/<id>` | Yes | Update lease item |
| `DELETE` | `/lease-items/<id>` | Yes | Delete lease item |
| `GET` | `/lease-items/categories` | No | Get categories |
| `POST` | `/chat` | No | Chatbot query |
| `POST` | `/mobile-activity` | No | Log mobile app activity |

> *Uses `mobileno` in body instead of token header.

---

## 10. Data Flow Diagrams

### User Authentication Flow

```
Browser                Flask Server            MongoDB
  │                        │                      │
  │── POST /users/login ──▶│                      │
  │   { mobileno, password}│                      │
  │                        │── find_one({mobileno})▶│
  │                        │◀─ user document ──────│
  │                        │                      │
  │                        │ check_password_hash()│
  │                        │ generate uuid token  │
  │                        │── update_one(token) ─▶│
  │◀── { token: uuid } ────│                      │
  │                        │                      │
  │ store token in         │                      │
  │ localStorage           │                      │
```

### Plant Disease Analysis Flow

```
Browser             Flask Server          HuggingFace       Groq API
  │                     │                    │                  │
  │─ POST /plant-disease│                    │                  │
  │  -analysis          │                    │                  │
  │  (multipart/image)  │                    │                  │
  │                     │ save image to      │                  │
  │                     │ uploads/           │                  │
  │                     │                    │                  │
  │                     │─ predict_disease() │                  │
  │                     │  MobileNetV2       │                  │
  │                     │  inference ───────▶│                  │
  │                     │◀─ {class, conf} ───│                  │
  │                     │                    │                  │
  │                     │─── LLaMA 3.3 prompt ─────────────────▶│
  │                     │    (disease details JSON)             │
  │                     │◀── structured JSON ────────────────────│
  │                     │                    │                  │
  │◀── {predictedDisease│                    │                  │
  │     confidence,     │                    │                  │
  │     analysis} ──────│                    │                  │
```

### Supply Chain Optimisation Flow

```
Browser             Flask Server          Mandi API        Haversine
  │                     │                    │                  │
  │─ POST /optimize-    │                    │                  │
  │  transport          │                    │                  │
  │  {city, crop, kg}   │                    │                  │
  │                     │─ fetch prices ────▶│                  │
  │                     │◀─ commodity prices ─│                  │
  │                     │                    │                  │
  │                     │─ for each city:    │                  │
  │                     │   calculate dist. ─────────────────── ▶│
  │                     │◀─ distance (km) ────────────────────── │
  │                     │   compute cost &   │                  │
  │                     │   net profit       │                  │
  │                     │                    │                  │
  │◀── optimisation ────│                    │                  │
  │    result + map_url │                    │                  │
```

---

## 11. External Integrations

### 1. Groq API (LLaMA 3.3 70B)

- **Purpose:** Powers crop recommendation, plant disease diagnosis, chatbot, and cost reduction suggestions.
- **Model used:** `llama-3.3-70b-versatile`
- **SDK:** Official Groq Python SDK.
- **API Key:** Set via `GROQ_API_KEY` environment variable.
- **Configuration per use case:**

| Feature | Temperature | Max Tokens |
|---------|------------|------------|
| Disease Analysis | 0.5 | 1024 |
| Crop Recommendation | 0.4 | 1024 |
| Chatbot | 0.7 | 400 |

### 2. Google Generative AI

- **Purpose:** Alternative LLM provider (imported but used as fallback).
- **SDK:** `google-generativeai` Python package.
- **API Key:** Set via `GOOGLE_API_KEY` environment variable.

### 3. Mandi API (Government of India Data Portal)

- **URL:** `https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070`
- **Purpose:** Real-time commodity/crop prices from Indian agricultural markets.
- **Fallback:** If the API is unavailable, simulated prices with ±5% variation are used.

### 4. Hugging Face Hub

- **Model:** `linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification`
- **Purpose:** Pre-trained plant disease classification model.
- **Downloaded via** the `transformers` library at server startup.

### 5. Haversine Library

- **Purpose:** Calculates the great-circle distance between two geographic coordinates (used for transport cost calculations).

---

## 12. Configuration & Environment Variables

### Frontend (`Frontend/.env`)

```env
VITE_API_URL=http://localhost:5000/api
```

| Variable | Default | Description |
|---------|---------|-------------|
| `VITE_API_URL` | `http://localhost:5000/api` | Base URL for all backend API calls |

### Backend (`Backend/.env`)

```env
MONGO_URI=mongodb://localhost:27017/shetniyojan
GROQ_API_KEY=<your-groq-api-key>
GOOGLE_API_KEY=<your-google-api-key>
```

| Variable | Required | Description |
|---------|---------|-------------|
| `MONGO_URI` | Yes | MongoDB connection string |
| `GROQ_API_KEY` | Yes | API key for Groq (LLaMA 3 access) |
| `GOOGLE_API_KEY` | No | API key for Google Generative AI |

---

## 13. Installation & Setup

### Prerequisites

| Requirement | Version |
|-----------|---------|
| Node.js | 16+ |
| npm | 8+ |
| Python | 3.8+ |
| MongoDB | 5.0+ |

### 1. Clone the Repository

```bash
git clone https://github.com/ninadsuryawanshi/ShetNiyojan.git
cd ShetNiyojan
```

### 2. Backend Setup

```bash
# Navigate to the Backend directory
cd Backend

# Create a Python virtual environment
python -m venv .venv

# Activate the environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install all Python dependencies
pip install -r requirements.txt

# Create the environment variables file
cp .env.example .env
# Edit .env and fill in MONGO_URI and GROQ_API_KEY

# Start the Flask development server
python app.py
```

The backend API will be available at `http://localhost:5000`.

### 3. Frontend Setup

```bash
# Navigate to the Frontend directory (from repo root)
cd Frontend

# Install npm dependencies
npm install

# Create the environment variables file
echo "VITE_API_URL=http://localhost:5000/api" > .env

# Start the Vite development server
npm run dev
```

The frontend will be available at `http://localhost:8080`.

### 4. Verify the Setup

1. Open `http://localhost:8080` in your browser.
2. Click **Register** and create an account.
3. Log in with your credentials.
4. You should be redirected to the Dashboard.

---

## 14. Available Scripts

### Frontend

```bash
npm run dev       # Start Vite development server on port 8080
npm run build     # Type-check and build production bundle
npm run preview   # Preview the production build locally
npm run lint      # Run ESLint on all TypeScript/TSX files
```

### Backend

```bash
python app.py     # Start Flask development server on port 5000
```

---

## 15. Security Considerations

### Current Implementation

| Area | Mechanism |
|------|-----------|
| Password storage | PBKDF2-HMAC-SHA256 via Werkzeug |
| Session management | UUID4 token stored in `users` collection |
| Token transmission | `x-access-token` header (not a cookie) |
| CORS | Enabled for all origins on `/api/*` |
| Input validation | Basic field presence checks |

### Known Limitations & Recommendations for Production

1. **CORS Policy:** Currently configured to allow all origins (`"*"`). For production, restrict to the specific frontend domain.
   ```python
   CORS(app, resources={r"/api/*": {"origins": "https://yourdomain.com"}})
   ```

2. **Development Auth Bypass:** The `token_required` middleware contains a development workaround that creates a fake user when no matching token is found in the database. **This must be removed before deploying to production.**

3. **Token Expiry:** UUID tokens currently have no expiry. Implement JWT with expiry claims or add a TTL index on the `token` field in MongoDB.

4. **HTTPS:** Ensure all production traffic is served over HTTPS to protect tokens in transit.

5. **API Key Security:** Groq and Google API keys must not be committed to version control. Use environment variable management solutions like AWS Secrets Manager or HashiCorp Vault in production.

6. **File Upload Security:** Uploaded images are saved to the `uploads/` directory without sanitisation of file names. Use `werkzeug.utils.secure_filename()` and validate MIME types before saving.

7. **Rate Limiting:** No rate limiting is implemented. Consider adding Flask-Limiter to protect the AI-powered endpoints from abuse.

8. **Input Sanitisation:** ML endpoints accept free-form numeric inputs without bounds checking. Add validation to prevent injection or unreasonable values.

---

## 16. Deployment Guide

### Docker (Recommended)

#### Backend `Dockerfile` (example)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

#### Frontend `Dockerfile` (example)

```dockerfile
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
```

#### `docker-compose.yml` (example)

```yaml
version: '3.8'
services:
  mongodb:
    image: mongo:6
    volumes:
      - mongo_data:/data/db

  backend:
    build: ./Backend
    ports:
      - "5000:5000"
    env_file: ./Backend/.env
    depends_on:
      - mongodb

  frontend:
    build:
      context: ./Frontend
      args:
        VITE_API_URL: http://backend:5000/api
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  mongo_data:
```

### Manual Deployment (VPS / Cloud VM)

1. **Provision a server** with Python 3.8+, Node.js 18+, and MongoDB 6.
2. **Clone the repository** and follow the setup steps in Section 13.
3. **Run the backend** with a production WSGI server:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
4. **Build the frontend:**
   ```bash
   npm run build
   ```
5. **Serve the `dist/` folder** using Nginx or Apache.
6. **Configure a reverse proxy** (Nginx) to route:
   - `/api/*` → `http://localhost:5000`
   - `/*` → frontend `dist/` directory

---

## 17. Future Enhancements

| Feature | Description | Priority |
|---------|-------------|---------|
| IoT Integration | Connect soil sensors and weather stations for real-time data input | High |
| Weather API | Integrate a live weather forecast API (OpenWeather, IMD) into the dashboard | High |
| JWT Authentication | Replace UUID tokens with JWT for built-in expiry and claims | High |
| Mobile App | React Native or Flutter app for offline-capable field use | Medium |
| Yield Analytics | Advanced charts for year-over-year yield comparison | Medium |
| Community Forum | Knowledge sharing between farmers | Medium |
| Government Scheme Alerts | Notify farmers about relevant government subsidies and schemes | Medium |
| Voice Input | Hindi/Marathi voice-to-text for hands-free operation in the field | Medium |
| Marketplace for Products | Sell harvested produce directly to buyers via the platform | Low |
| Offline Mode | PWA with service workers for offline data collection | Low |

---

## 18. Contributors

| Name | Role |
|------|------|
| Ninad Suryawanshi | Project Lead, Backend Developer |
| Gopal Dose | Backend Developer, ML Engineer |
| Yuvraj Sanghai | Frontend Developer |
| Shreeshail Chavan | Frontend Developer |
| Viraj Mane | UI/UX Designer, Frontend Developer |

---

*This documentation was generated based on analysis of the ShetNiyojan codebase. Last updated: March 2026.*
