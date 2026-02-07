#!/usr/bin/env python3
"""Test script to check argon2 functionality"""

from passlib.context import CryptContext

try:
    # Initialize the context with argon2
    pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
    print("CryptContext with argon2 initialized successfully")

    # Test hashing a short password
    password = "wasif123"
    print(f"Testing password: '{password}' (length: {len(password)})")

    hashed = pwd_context.hash(password)
    print(f"Password hashed successfully: {hashed[:20]}...")

    # Test verification
    verified = pwd_context.verify(password, hashed)
    print(f"Password verification: {verified}")

    print("Argon2 test completed successfully!")

except Exception as e:
    print(f"Argon2 test failed: {e}")
    import traceback
    traceback.print_exc()