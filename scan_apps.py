from commands.app_scanner import scan_apps

print("=" * 50)
print("JARVIS APP SCANNER")
print("=" * 50)

apps = scan_apps()

print(f"\nFound {len(apps)} applications.\n")

for app in sorted(apps.keys()):
    print(app)

print("\nScan Completed Successfully!")