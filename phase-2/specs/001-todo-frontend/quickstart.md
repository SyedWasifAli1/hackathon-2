# Quick Start Guide: Full-Stack Todo Application (Frontend)

## Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- Access to the backend API server (running on http://localhost:8000)

## Setup Instructions

### 1. Clone and Navigate to Frontend Directory
```bash
cd frontend
```

### 2. Install Dependencies
```bash
npm install
# or
yarn install
```

### 3. Environment Configuration
Create a `.env.local` file in the frontend directory with the following:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

### 4. Run Development Server
```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`

## Key Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run linter

## Project Structure

```
frontend/
├── app/                    # Next.js App Router pages
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Home page
│   ├── auth/               # Authentication pages
│   │   ├── login/page.tsx
│   │   └── register/page.tsx
│   └── dashboard/          # Protected routes
│       ├── layout.tsx      # Protected layout
│       ├── page.tsx        # Dashboard home
│       └── todos/page.tsx  # Todo management
├── components/            # Reusable components
│   ├── ui/                # Basic UI components
│   ├── layout/            # Layout components
│   ├── auth/              # Authentication components
│   └── todos/             # Todo-specific components
├── context/               # React Context providers
│   └── AuthContext.tsx    # Authentication state
├── services/              # API services
│   ├── api.ts             # Axios configuration
│   ├── auth.service.ts    # Authentication API calls
│   └── todo.service.ts    # Todo API calls
├── hooks/                 # Custom React hooks
│   ├── useAuth.ts         # Authentication hook
│   └── useTodos.ts        # Todo management hook
├── styles/                # Global styles
│   └── globals.css        # Tailwind and custom styles
├── middleware.ts          # Route protection
├── tailwind.config.ts     # Tailwind configuration
└── package.json
```

## Development Guidelines

### Component Structure
- Use functional components with TypeScript
- Implement proper TypeScript interfaces
- Separate UI components from feature components
- Follow the Arctic Frost theming guidelines

### API Integration
- All API calls should go through service files
- Use Axios with interceptors for JWT handling
- Implement proper error handling
- Handle loading states appropriately

### Authentication Flow
1. User registers/logs in via auth forms
2. JWT token is stored in localStorage
3. AuthContext updates global state
4. Protected routes verify authentication
5. Token refresh/logout handled automatically

### Theming
- Use Tailwind utility classes consistently
- Apply Arctic Frost color palette
- Implement glassmorphism effects with backdrop-filter
- Ensure responsive design for all screen sizes