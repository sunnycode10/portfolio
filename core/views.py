from django.shortcuts import render
from .models import HeroSection, AboutSection
from portfolio.models import Project
from experience.models import Skill, Job

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from openai import OpenAI
from django.conf import settings
import os
from groq import Groq
from django.http import StreamingHttpResponse


# client = OpenAI(api_key=settings.OPENAI_API_KEY)





def home(request):
    hero = HeroSection.objects.first()
    about = AboutSection.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    jobs = Job.objects.all()
    
    context = {
        'hero': hero,
        'about': about,
        'projects': projects,
        'skills': skills,
        'jobs': jobs,
    }
    return render(request, 'temp/index.html', context)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def build_portfolio_context():
    projects = Project.objects.all()
    skills = Skill.objects.all()

    project_text = "\n".join([
        f"- {p.title}: {p.description} (Tech: {p.tech_stack})"
        for p in projects
    ])

    skill_text = ", ".join([s.name for s in skills])

    return f"""
Sunny is a professional software developer.

Skills:
{skill_text}

Projects:
{project_text}

Contact:
Email: sunnyemmanuel5@gmail.com
"""

@csrf_exempt
def chat_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    data = json.loads(request.body)
    user_message = data.get("message", "")

    context = build_portfolio_context()

    system_prompt = f"""
You are SunnyBot, the AI assistant for Sunny's portfolio.

Rules:
- Use ONLY the portfolio context.
- Respond clearly and concisely.
- Use markdown: **bold**, bullet points, line breaks.
- If asked about contact, provide: sunnyemmanuel5@gmail.com.

Portfolio Context:
{context}
"""


    def stream():
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            stream=True,
        )

        for chunk in completion:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                yield delta.content

    return StreamingHttpResponse(stream(), content_type="text/plain")

def about(request):
    about_data = AboutSection.objects.first()
    jobs = Job.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'about': about_data,
        'jobs': jobs,
        'skills': skills,
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    return render(request, 'pages/contact.html')


 