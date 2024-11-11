# **Borderless Fullscreen Toggle Script for MelonDS and Lime3DS Emulators**

This Python script allows you to toggle the borderless fullscreen mode of the **MelonDS** and **Lime3DS** emulator windows across multiple monitors by pressing the **F7** key. It automatically adjusts the emulator window to cover all connected screens without the need to manually specify screen resolutions or configurations.

### **How It Works**

- **Toggle with F7**: Press the **F7** key to switch the emulator window between normal mode and borderless fullscreen mode.
- **Automatic Screen Detection**: The script detects all connected monitors and calculates the total screen area, regardless of their resolutions or arrangements (horizontal or vertical).
- **Window Adjustment**: It removes the window borders and title bar of the emulator, then resizes and moves it to cover the entire screen area.
- **State Restoration**: Pressing **F7** again restores the window to its original size, position, and style.

### **Dependencies**

To run this script, you need to have the following Python packages installed:

- **pygetwindow**: For window manipulation.
  ```bash
  pip install pygetwindow

- **keyboard**: To detect key presses.
  ```bash
  pip install keyboard

- **screeninfo**: To get information about connected monitors.
  ```bash
  pip install screeninfo

- **pywin32**: For Windows-specific window styling.
  ```bash
  pip install pywin32

**Note**: This script is intended for use on **Windows** operating systems due to the use of Windows APIs.

### **Recommended Settings for Optimal Results with Spacedesk on Smartphones**

For a perfect experience when using **Spacedesk** to extend your display to a smartphone, it's recommended to:

1. **Set the Second Extended Screen in Vertical Orientation**: This ensures that the emulator displays correctly on the smartphone screen.

2. **Configure the Emulator's Screen Settings as Follows**:

   - **For MelonDS**:
     - **Screen Rotation**: `0`
     - **Screen Gap**: `0`
     - **Screen Layout**: `0`
     - **Screen Sizing**: `Even`
     - **Aspect Ratio**:
       - **Top**: `4:3 (native)`
       - **Bottom**: `4:3 (native)`

   - **For Lime3DS**:
     - **Screen Layout**: `Default`

These settings help in aligning the emulator's dual screens perfectly across your main monitor and the extended smartphone display, providing a seamless gaming experience.

### **Usage Instructions**

1. **Start the Emulator**: Open either **MelonDS** or **Lime3DS** and ensure the emulator window is visible on your desktop.

2. **Run the Script**: Execute the Python script in your preferred environment.

3. **Toggle Fullscreen Mode**:

   - Press **F7** to switch the emulator window to borderless fullscreen mode across all connected screens.
   - Press **F7** again to restore the window to its original state with borders.

4. **Exit the Script**: Press **Esc** to terminate the script when you're finished.

### **Important Notes**

- **Window Titles**: The script searches for windows titled **`melonDS`** and **`Lime3DS`**. If your emulator window has a different title, you may need to modify the `window_titles` list in the script to match it.

- **Permissions**: The script may require administrative permissions to interact with other application windows. Run your Python environment as an administrator if you encounter permission issues.

- **Compatibility**: This script is designed for **Windows** systems due to the use of Windows-specific APIs in the **pywin32** library.

### **Troubleshooting**

- **Emulator Window Not Found**: If the script cannot find the emulator window, make sure:

  - The emulator is running.
  - The window is not minimized.
  - The window title matches exactly (**`melonDS`** or **`Lime3DS`**).

- **Dependencies Not Installed**: If you receive import errors, ensure all required Python packages are installed using the `pip install` commands provided in the **Dependencies** section.

- **Script Not Responding**: Ensure that no other application is capturing the **F7** key. Also, check that the script is running in the foreground.

### **Customization**

- **Adding More Applications**: To extend this script to work with other applications, add their window titles to the `window_titles` list in the script.

- **Modifying Hotkey**: To change the hotkey from **F7** to another key, modify the `'F7'` argument in the `keyboard.add_hotkey` function.

### **Conclusion**

This script provides a convenient way to enhance your emulator experience by allowing you to quickly toggle between normal and borderless fullscreen modes. It's especially useful when using multiple monitors or extending your display to devices like smartphones via **Spacedesk**.

Feel free to customize and improve the script to suit your needs. Contributions are welcome!

---

**Disclaimer**: Use this script responsibly and ensure that you comply with all relevant software licenses and terms of service when using emulators and other software.

