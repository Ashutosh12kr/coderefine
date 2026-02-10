# CodeRefine AI 🚀

CodeRefine is a powerful, AI-driven code review and optimization engine. It leverages Google's Gemini Pro model to analyze code snippets, identify potential bugs, suggest style improvements, and provide optimized versions of your code with detailed explanations.

![Project Preview](https://via.placeholder.com/800x400?text=CodeRefine+AI+Interface) *(Note: Add your actual screenshot here after deployment!)*

## ✨ Features

- **Code Review:** Detailed analysis of logic, readability, and best practices.
- **Bug Detection:** Identifies potential runtime errors and logical flaws.
- **Performance Optimization:** Suggests more efficient ways to write your algorithms.
- **Multi-Language Support:** Works with Python, JavaScript, Java, and C++.
- **Modern UI:** Sleek, glassmorphism-inspired dark mode interface.
- **Vercel Ready:** Pre-configured for seamless monorepo deployment.

## 🛠️ Tech Stack

- **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript.
- **Backend:** Python, FastAPI, Uvicorn.
- **AI Engine:** Google Generative AI (Gemini-1.5-Flash).
- **Deployment:** Optimized for Vercel.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- A Google AI Studio API Key (Get one at [aistudio.google.com](https://aistudio.google.com/))

### Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ashutosh12kr/coderefine.git
   cd coderefine
   ```

2. **Setup Backend:**
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment:**
   Create a `.env` file in the `backend` folder and add your API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the Application:**
   - **Start Backend:** `python main.py` (Runs on port 8000)
   - **Start Frontend:** Open `frontend/index.html` in your browser or run a local server: `cd frontend && python -m http.server 8080`.

## ☁️ Deployment (Vercel)

This project is configured as a monorepo. To deploy:

1. Push your code to GitHub.
2. Import the project into [Vercel](https://vercel.com).
3. Vercel will automatically detect the `vercel.json` and deploy both the frontend and the serverless backend functions.
4. **Environment Variable:** Add `GEMINI_API_KEY` in your Vercel project settings.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---
Built with ❤️ by [Ashutosh Kumar](https://github.com/Ashutosh12kr)
