# Contributing to YTConverter™

First off, thank you for considering contributing to **YTConverter™**! Your support is invaluable in making this tool even more robust and user-friendly.

## 🛠️ Getting Started

1.  **Fork the Repository** Click the "Fork" button at the top right of the [repository page](https://github.com/kaifcodec/ytconverter).

2.  **Clone Your Fork**
    ```bash
    git clone https://github.com/your-username/ytconverter.git
    cd ytconverter
    ```

3.  **Set Up the Environment**

    **For Termux:**

    ```bash
    pkg update -y && pkg upgrade -y
    pkg install python git curl
    termux-setup-storage
    pip install -r requirements.txt
    ```

    **For Linux (Ubuntu/Debian/Fedora/Arch):**

    ```bash
    sudo apt update && sudo apt install python3 python3-pip git curl -y
    pip3 install -r requirements.txt
    ```

4.  **Run the Application**

    ```bash
    python ytconverter.py
    ```
## 🚧 Areas Where Help Is Needed

We’re currently looking for contributors to help with:

- **Modularizing the codebase**: Breaking down the monolithic script (`ytconverter.py`) into smaller, manageable modules.
- **Improving testability**: Making the code easier to test, possibly by refactoring away from `input()` toward CLI arguments or config-driven options.
- **Modernizing dependencies**: Replacing older libraries like [`requests`](https://pypi.org/project/requests/), [`colored`](https://pypi.org/project/colored/), and [`fontstyle`](https://pypi.org/project/fontstyle/) with more modern and performant alternatives such as [`httpx`](https://pypi.org/project/httpx/) and [`rich`](https://pypi.org/project/rich/).

- **Building a Web GUI (Frontend Help Wanted)**:

We’re excited to welcome contributors who want to build a clean, user-friendly web interface for **YTConverter™**. This is your chance to design the experience — feel free to implement your own ideas and UI logic!

To get you started, here’s a very rough sketch of how the backend might work, but you’re absolutely encouraged to adapt or redesign it however you see fit:

- A typical flow could include:
  - Input for video URL
  - Options for format selection (e.g., MP3, MP4)
  - Quality preferences (high, medium, low, etc.)
  - Display of download progress and status
  - Download button when ready

- On the backend side, there might be endpoints like:
  - `POST /api/download` to start the process
  - `GET /api/status/{task_id}` to check progress

But feel free to suggest improvements or create alternative approaches that best fit your frontend design.

Your creativity and expertise are what will truly make the app shine — so no pressure to strictly follow the current backend. We’re here to support you in integrating your frontend with the backend smoothly.

Thank you in advance for helping make **YTConverter™** more accessible and enjoyable for everyone!

## 🧪 Running Tests

Before submitting your changes, ensure that:

* The application runs without errors.
* New features or fixes are covered by tests, if applicable.
* Existing tests pass successfully.


## 🔀 Branching Strategy

* `main`: Stable release branch.
* `dev`: Development branch for ongoing work.
* `feature/<your-feature-name>`: Prefix for new feature branches (e.g., `feature/add-download-option`).
* `bugfix/<your-bug-fix>`: Prefix for bug fix branches (e.g., `bugfix/fix-crash-on-startup`).

## ✅ Commit Messages


Use clear and concise commit messages. Follow this format:
**Example:**


feat: add support for batch video downloads
Implemented functionality to allow users to download random music according to their mood, several random quotes.

**Types:**

* `feat`: New feature
* `fix`: Bug fix
* `docs`: Documentation changes
* `style`: Code style changes (formatting, missing semicolons, etc.)
* `refactor`: Code refactoring
* `test`: Adding or updating tests
* `chore`: Maintenance tasks




## 📬 Submitting a Pull Request

1.  **Ensure your fork is up to date:**

    ```bash
    git checkout main
    git pull upstream main
    ```

2.  **Create a new branch for your feature or fix:**

    ```bash
    git checkout -b feature/your-feature-name
    ```

3.  **Make your changes and commit them:**

    ```bash
    git add .
    git commit -m "feat: add your feature"
    ```

4.  **Push your branch to your fork:**

    ```bash
    git push origin feature/your-feature-name
    ```

5.  **Open a Pull Request on GitHub:**

    * Go to your forked repository.
    * Click on "Compare & pull request".
    * Provide a clear description of your changes.

## 📞 Contact

For any questions or discussions:

* **Email:** kaifcodec@gmail.com
* **Issues:** Submit an issue on [GitHub](https://github.com/kaifcodec/ytconverter/issues)

