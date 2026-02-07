import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

export function proxy(request: NextRequest) {
  const token = request.cookies.get("token")?.value;
  const { pathname } = request.nextUrl;

  // Pages that do NOT require auth
  const publicPaths = ["/login", "/register"];

  // If the request is for login/register page
  if (publicPaths.some((path) => pathname.startsWith(path))) {
    // If already logged in → redirect to dashboard
    if (token) {
      return NextResponse.redirect(new URL("/", request.url));
    }
    return NextResponse.next();
  }

  // All other routes → protected
  if (!token) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  // Allow request
  return NextResponse.next();
}

// Match everything except Next.js internal and API routes
export const config = {
  matcher: ["/((?!_next|favicon.ico|api).*)"],
};