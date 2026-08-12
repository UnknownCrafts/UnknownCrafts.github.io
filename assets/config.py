# assets/config.py
from dataclasses import dataclass


@dataclass
class NavItem:
    icon: str
    title: str
    description: str
    href: str


SITE = {
    "name": "Surya Vasudev",
    "tagline": "Computer Engineering Student & Full-Stack Developer",
    "subtitle": "Living on the bleeding edge of tech, building robust systems, and competing in hackathons.",
    "github": "https://github.com/UnknownCrafts",
    "gitlab": "https://gitlab.com/suryavasudev005",
    "linkedin": "https://linkedin.com/in/surya-vasudev-b12547239/",
}

NAV_ITEMS = [
    NavItem("briefcase", "Experiences", "My professional journey", "/experience"),
    NavItem("folder-git-2", "Projects", "Things I've built", "/projects"),
    NavItem("pen-tool", "Blog", "Thoughts and writings", "/blogs"),
    NavItem("github", "GitHub", "Code repositories", SITE["github"]),
    NavItem("gitlab", "GitLab", "Secondary repositories", SITE["gitlab"]),
    NavItem("linkedin", "LinkedIn", "Professional network", SITE["linkedin"]),
]
