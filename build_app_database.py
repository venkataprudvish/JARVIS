from commands.app_engine import build_database

print("=" * 50)
print("JARVIS APP ENGINE")
print("=" * 50)

apps = build_database()

print("\nApp Database Built Successfully!")
print(f"Total Apps Found: {len(apps)}")