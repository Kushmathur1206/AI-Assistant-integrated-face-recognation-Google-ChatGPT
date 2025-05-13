# Desktop-AI-Assistant-Google-ChatGPT-Uses-face-recognation-to-identify-the-person

AI Assistant with Face Recognition + Google + ChatGPT Integration
This project is a multimodal AI assistant that combines face recognition, voice interaction, Google search, and ChatGPT responses to provide a personalized, intelligent assistant experience. It supports real-time face authentication and performs voice-command-based task execution with the help of OpenAI's GPT model and Google APIs.

Features
- Face Recognition-Based Access Control
- Uses a webcam to authenticate the user via real-time face recognition using face_recognition and OpenCV.
- AI-Powered Chat & Query Handling

After authentication, the assistant listens for voice input, converts it to text, and intelligently responds using:
- Google Search (for general knowledge/factual queries)
- ChatGPT (OpenAI API) (for conversational and creative tasks)

Voice Interaction
The assistant speaks its responses using pyttsx3 (text-to-speech), creating a smooth interactive experience.

Wake Word Detection
It can remain passive until a specific "wake word" (like "hey assistant") is spoken.

Tech Stack
Face Recognition	face_recognition, OpenCV
Voice Input	speech_recognition
Voice Output	pyttsx3
AI Chat	openai (ChatGPT API)
Web Search	pywhatkit, googlesearch-python
Other Utils	os, datetime, webbrowser
