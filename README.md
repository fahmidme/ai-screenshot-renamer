# AI-Powered Screenshot Renamer

This project automatically renames screenshots using AI-generated descriptions. It's designed to work with macOS and uses OpenAI's GPT-4 Vision model to analyze and describe screenshots.

## Features

- Automatically detects new screenshots
- Uses AI to generate descriptive names for screenshots
- Renames files with the format: `description_YYYY-MM-DD.png`
- Logs actions for debugging

## Prerequisites

- macOS
- Python 3.7+
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-screenshot-renamer.git
   cd ai-screenshot-renamer
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Setup

### Configure macOS to Save Screenshots to Documents/screenshots

1. Create the screenshots directory:
   ```
   mkdir -p ~/Documents/screenshots
   ```

2. Change the default screenshot save location:
   ```
   defaults write com.apple.screencapture location ~/Documents/screenshots
   ```

3. Restart the SystemUIServer to apply changes:
   ```
   killall SystemUIServer
   ```

### Set Up Folder Action with Automator

1. Open Automator and create a new Folder Action:
   - Launch Automator from your Applications folder.
   - Choose "New Document" and select "Folder Action" as the type.

2. Configure the Folder Action:
   - At the top of the window, set "Folder Action receives files and folders added to" to your screenshots folder (e.g., `~/Documents/screenshots`).

3. Add a "Run Shell Script" action:
   - In the left sidebar, search for "Run Shell Script" and drag it into the workflow area.

4. Configure the Shell Script action:
   - Set "Shell" to `/bin/zsh`
   - Set "Pass input" to "as arguments"
   - Copy the contents of `screenshot_action.sh` into the script area.

5. Save the Folder Action:
   - Choose File > Save, name it "Screenshot Renamer", and click Save.

## Usage

After setup, the system will automatically process new screenshots:

1. Take a screenshot (Cmd + Shift + 3 or Cmd + Shift + 4).
2. The screenshot will be saved to `~/Documents/screenshots`.
3. The Folder Action will trigger the renaming script.
4. The screenshot will be renamed with an AI-generated description and timestamp.

## Troubleshooting

Check the `debug_log.txt` file in the project directory for detailed logs if you encounter any issues.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is released under the Unlicense. See the [LICENSE](LICENSE) file for details.