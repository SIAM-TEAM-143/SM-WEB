import platform

if platform.architecture()[0] != "64bit":
    print("32bit Not Supported!")
else:
    try:
        import smx

        # Start the module's main entry point
        if hasattr(smx, "main_menu"):
            smx.main_menu()
        elif hasattr(smx, "main"):
            smx.main()
        else:
            print("Error:  function.")

    except Exception as e:
        import traceback
        print(f"\nCRITICAL ERROR: {e}")
        traceback.print_exc()
        input("\nPress Enter to exit...")
