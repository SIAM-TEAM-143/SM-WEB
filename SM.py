import platform

if platform.architecture()[0] != "64bit":
    print("32bit Not Supported!")
else:
    try:
        import metav10

        # Start the module's main entry point
        if hasattr(metav10, "main_menu"):
            metav10.main_menu()
        elif hasattr(metav10, "main"):
            metav10.main()
        else:
            print("Error: xotp has no main_menu() or main() function.")

    except Exception as e:
        import traceback
        print(f"\nCRITICAL ERROR: {e}")
        traceback.print_exc()
        input("\nPress Enter to exit...")
