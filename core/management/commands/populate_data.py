from django.core.management.base import BaseCommand
from core.models import HeroSection, AboutSection
from portfolio.models import Project
from experience.models import Job, Skill
from django.utils.text import slugify
from datetime import date

class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating data...')

        # Hero Section
        HeroSection.objects.all().delete()
        HeroSection.objects.create(
            title="Hello, I'm SunnyCode",
            subtitle="Software Engineer & DevOps Specialist"
        )

        # About Section
        AboutSection.objects.all().delete()
        AboutSection.objects.create(
            bio="""A passionate software engineer skilled in Django, Python, JavaScript, React, and DevOps. Experienced in API development, frontend implementation, cloud infrastructure, and managing full web application lifecycles. Strong background in IT infrastructure, project management, user interface design, and cross-team collaboration.

Name: Sunday Emmanuel Emenike
Brand Name: SunnyCode
Address: 11 Kusenla Rd, Ikate Elegushi, Lekki, Lagos
Email: sunnyemmanuel5@gmail.com
Phone: 07083659432 / 08154431918
GitHub: https://github.com/sunnyemmanuel"""
        )

        # Skills
        Skill.objects.all().delete()
        skills_data = [
            ('Django', 'WEB', 95),
            ('Django REST Framework', 'WEB', 90),
            ('React.js', 'WEB', 85),
            ('JavaScript', 'WEB', 85),
            ('Python', 'WEB', 95),
            ('API development', 'WEB', 90),
            ('Docker', 'TOOLS', 80),
            ('AWS', 'TOOLS', 75),
            ('Project Research', 'OTHER', 85),
            ('Project Management (Asana, Jira)', 'OTHER', 80),
            ('Graphic Design (Adobe Photoshop & Illustrator)', 'OTHER', 70),
            ('Microsoft Office suite', 'OTHER', 90),
        ]
        for name, category, proficiency in skills_data:
            Skill.objects.create(name=name, category=category, proficiency=proficiency)

        # Jobs
        Job.objects.all().delete()
        jobs_data = [
            ('Vetry Technologies Ltd (VT)', 'Head of IT', date(2024, 1, 1), None, True, 'Leading IT infrastructure and software development.'),
            ('Wakaati NG Limited', 'Software Engineer / Facilitator', date(2023, 1, 1), date(2024, 1, 1), False, 'Developed web applications and facilitated training.'),
            ('Summit AI (Contract)', 'Backend Engineer / DevOps', date(2018, 1, 1), date(2020, 1, 1), False, 'Managed backend services and cloud infrastructure.'),
            ('Diamond Acre Software (DAS)', 'Junior Software Engineer', date(2018, 1, 1), date(2020, 1, 1), False, 'Assisted in software development and testing.'),
            ('Grace First Property', 'Facility Manager', date(2017, 1, 1), date(2017, 12, 31), False, 'Managed facility operations.'),
            ('Hip-Touch Solutions Limited', 'Logistics / Procurement Officer', date(2012, 1, 1), date(2013, 1, 1), False, 'Handled logistics and procurement.'),
        ]
        for company, role, start, end, current, desc in jobs_data:
            Job.objects.create(
                company=company,
                role=role,
                start_date=start,
                end_date=end,
                is_current=current,
                description=desc
            )

        # Projects
        Project.objects.all().delete()
        projects_data = [
            ('Got Laundry Delivers', 'https://gotlaundrydelivers.com/', 'Laundry delivery service platform.', 'Django, React'),
            ('Nonstop Source', 'https://nonstopsource.com/', 'Sourcing platform.', 'Django, AWS'),
            ('Vetry Tech', 'https://vetrytech.com/', 'Corporate website for Vetry Technologies.', 'Django, Tailwind'),
            ('Stowpoint', 'https://stowpoint.co.uk/', 'Storage solutions platform.', 'Python, Flask'),
            ('Summit Guide', 'https://summit.guide/', 'Guide and resource platform.', 'React, Node.js'),
            ('MoveIn NG', 'https://movein.ng', 'Real estate platform.', 'Django, PostgreSQL'),
        ]
        for i, (title, link, desc, stack) in enumerate(projects_data):
            Project.objects.create(
                title=title,
                slug=slugify(title),
                description=desc,
                tech_stack=stack,
                live_link=link,
                order=i
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated data'))
