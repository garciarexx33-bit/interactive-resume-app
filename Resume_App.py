"""
Program: Resume_App.py
Author: Pedro Ledezma"""


import tkinter as tk
from tkinter import messagebox
import webbrowser


class ResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pedro Ledezma | Interactive Resume")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)
        self.root.configure(bg="#eef1f5")

        self.selected_section = tk.StringVar(value="About Me")

        self.sections = {
            "About Me": self.about_me_text(),
            "Education": self.education_text(),
            "Skills": self.skills_text(),
            "FightLine": self.fightline_text(),
            "Anton / Bapa": self.anton_text(),
            "Data Manager": self.data_manager_text(),
            "Leadership": self.leadership_text(),
        }

        self.create_header()
        self.create_main_area()
        self.create_footer()
        self.display_section()

    def create_header(self):
        header = tk.Frame(self.root, bg="#172033", height=125)
        header.pack(fill="x")
        header.pack_propagate(False)

        name_label = tk.Label(
            header,
            text="PEDRO LEDEZMA",
            font=("Arial", 26, "bold"),
            bg="#172033",
            fg="white",
        )
        name_label.pack(pady=(18, 3))

        title_label = tk.Label(
            header,
            text="Computer Science Student | Python Developer",
            font=("Arial", 13),
            bg="#172033",
            fg="#cbd5e1",
        )
        title_label.pack()

        contact_label = tk.Label(
            header,
            text=(
                "San Diego, CA   •   garciarexx33@gmail.com"
            ),
            font=("Arial", 10),
            bg="#172033",
            fg="#94a3b8",
        )
        contact_label.pack(pady=7)

    def create_main_area(self):
        main_frame = tk.Frame(self.root, bg="#eef1f5")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_navigation(main_frame)
        self.create_content_area(main_frame)

    def create_navigation(self, parent):
        navigation = tk.Frame(
            parent,
            bg="#ffffff",
            width=230,
            highlightthickness=1,
            highlightbackground="#d7dce2",
        )
        navigation.pack(side="left", fill="y", padx=(0, 18))
        navigation.pack_propagate(False)

        menu_title = tk.Label(
            navigation,
            text="RESUME SECTIONS",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            fg="#334155",
        )
        menu_title.pack(anchor="w", padx=20, pady=(24, 12))

        for section in self.sections:
            radio = tk.Radiobutton(
                navigation,
                text=section,
                variable=self.selected_section,
                value=section,
                command=self.display_section,
                font=("Arial", 11),
                bg="#ffffff",
                fg="#1e293b",
                activebackground="#ffffff",
                activeforeground="#2563eb",
                selectcolor="#dbeafe",
                anchor="w",
                cursor="hand2",
                padx=10,
                pady=8,
            )
            radio.pack(fill="x", padx=12)

        separator = tk.Frame(navigation, bg="#e2e8f0", height=1)
        separator.pack(fill="x", padx=20, pady=18)

        github_button = tk.Button(
            navigation,
            text="Open GitHub",
            command=self.open_github,
            font=("Arial", 10, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            pady=10,
        )
        github_button.pack(fill="x", padx=20)

        email_button = tk.Button(
            navigation,
            text="Send Email",
            command=self.send_email,
            font=("Arial", 10, "bold"),
            bg="#475569",
            fg="white",
            activebackground="#334155",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            pady=10,
        )
        email_button.pack(fill="x", padx=20, pady=(10, 0))

        copy_button = tk.Button(
            navigation,
            text="Copy Current Section",
            command=self.copy_section,
            font=("Arial", 10),
            bg="#e2e8f0",
            fg="#1e293b",
            activebackground="#cbd5e1",
            cursor="hand2",
            relief="flat",
            pady=10,
        )
        copy_button.pack(fill="x", padx=20, pady=(10, 0))

    def create_content_area(self, parent):
        content_card = tk.Frame(
            parent,
            bg="#ffffff",
            highlightthickness=1,
            highlightbackground="#d7dce2",
        )
        content_card.pack(side="right", fill="both", expand=True)

        self.section_title = tk.Label(
            content_card,
            text="",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#172033",
            anchor="w",
        )
        self.section_title.pack(fill="x", padx=35, pady=(30, 10))

        title_line = tk.Frame(content_card, bg="#2563eb", height=3)
        title_line.pack(fill="x", padx=35, pady=(0, 20))

        text_container = tk.Frame(content_card, bg="#ffffff")
        text_container.pack(fill="both", expand=True, padx=30, pady=(0, 25))

        scrollbar = tk.Scrollbar(text_container)
        scrollbar.pack(side="right", fill="y")

        self.content_text = tk.Text(
            text_container,
            wrap="word",
            font=("Arial", 12),
            bg="#ffffff",
            fg="#334155",
            relief="flat",
            padx=8,
            pady=8,
            spacing1=3,
            spacing3=7,
            yscrollcommand=scrollbar.set,
        )
        self.content_text.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.content_text.yview)

        self.content_text.tag_configure(
            "section_heading",
            font=("Arial", 14, "bold"),
            foreground="#1d4ed8",
            spacing1=12,
            spacing3=6,
        )

        self.content_text.tag_configure(
            "body",
            font=("Arial", 12),
            foreground="#334155",
            spacing3=7,
        )

        self.content_text.tag_configure(
            "bullet",
            font=("Arial", 12),
            foreground="#334155",
            lmargin1=10,
            lmargin2=28,
            spacing3=6,
        )

    def create_footer(self):
        footer = tk.Label(
            self.root,
            text="Built with Python and Tkinter",
            font=("Arial", 9),
            bg="#172033",
            fg="#94a3b8",
            pady=7,
        )
        footer.pack(fill="x")

    def display_section(self):
        section = self.selected_section.get()
        content = self.sections.get(section, "")

        self.section_title.config(text=section)

        self.content_text.config(state="normal")
        self.content_text.delete("1.0", tk.END)

        lines = content.split("\n")

        for line in lines:
            if line.startswith("## "):
                self.content_text.insert(
                    tk.END,
                    line.replace("## ", "") + "\n",
                    "section_heading",
                )
            elif line.startswith("• "):
                self.content_text.insert(
                    tk.END,
                    line + "\n",
                    "bullet",
                )
            else:
                self.content_text.insert(
                    tk.END,
                    line + "\n",
                    "body",
                )

        self.content_text.config(state="disabled")
        self.content_text.yview_moveto(0)

    def copy_section(self):
        section = self.selected_section.get()
        content = self.sections.get(section, "")

        clean_content = content.replace("## ", "")

        self.root.clipboard_clear()
        self.root.clipboard_append(clean_content)

        messagebox.showinfo(
            "Section Copied",
            f"The {section} section was copied to your clipboard.",
        )

    @staticmethod
    def open_github():
        webbrowser.open("https://github.com/garciarexx33-bit")

    @staticmethod
    def send_email():
        webbrowser.open("mailto:garciarexx33@gmail.com")

    @staticmethod
    def about_me_text():
        return (
            "Hi, I'm Pedro. I'm currently studying Computer Science at "
            "San Diego Mesa College, where I've been building projects that "
            "help me grow as a programmer and problem-solver.\n\n"
            "I enjoy creating useful Python applications, working with APIs, "
            "building desktop interfaces with Tkinter, and figuring out why "
            "something is not working when a bug appears.\n\n"
            "Most of my experience has come from hands-on projects. I've built "
            "an MMA odds tracker, a personal terminal assistant, and a desktop "
            "data-management program. Every project has helped me become more "
            "comfortable writing cleaner code, organizing larger programs, "
            "and creating software that is easier for people to use.\n\n"
            "I'm looking for an entry-level opportunity where I can keep "
            "learning, contribute to a team, and prove that I can be a "
            "reliable asset."
        )

    @staticmethod
    def education_text():
        return (
            "## San Diego Mesa College\n"
            "San Diego, California\n\n"
            "Associate Degree in Computer Science\n"
            "Expected Graduation: 2027\n\n"
            "## Relevant Coursework\n"
            "• Introduction to Computer Science\n"
            "• Python Programming\n"
            "• C++ Programming\n"
            "• Trigonometry\n"
            "• Calculus\n"
            "• Linear Algebra\n\n"
            "My coursework has helped me build a foundation in programming, "
            "problem-solving, mathematics, and software development."
        )

    @staticmethod
    def skills_text():
        return (
            "## Programming Languages\n"
            "• Python\n"
            "• C++\n\n"
            "## Desktop Interface Development\n"
            "• Tkinter\n"
            "• Radio buttons\n"
            "• Command buttons\n"
            "• Entry fields\n"
            "• Labels and frames\n"
            "• Scrollbars\n"
            "• Message boxes\n"
            "• Event-driven programming\n\n"
            "## Tools and Technologies\n"
            "• Git\n"
            "• GitHub\n"
            "• Visual Studio Code\n"
            "• REST APIs\n"
            "• JSON data\n"
            "• Command-line tools\n"
            "• File input and output\n\n"
            "## Strengths\n"
            "• Debugging and troubleshooting\n"
            "• Breaking large problems into smaller steps\n"
            "• Organizing code into separate files and modules\n"
            "• Learning new tools through hands-on practice\n"
            "• Staying patient when solving technical problems\n\n"
            "## Certification in Progress\n"
            "• Microsoft SC-900: Security, Compliance, and Identity Fundamentals"
        )

    @staticmethod
    def fightline_text():
        return (
            "## FightLine\n"
            "Python Developer | 2026–Present\n\n"
            "FightLine started as a way for me to combine two things I enjoy: "
            "programming and MMA.\n\n"
            "I built a Python desktop application that pulls live betting "
            "odds from multiple sportsbooks and displays the information in "
            "an organized Tkinter interface.\n\n"
            "## What I Built\n"
            "• Connected the application to The Odds API\n"
            "• Retrieved and processed live sportsbook data\n"
            "• Displayed betting odds inside a Tkinter interface\n"
            "• Added automatic refreshing for updated odds\n"
            "• Tracked betting-line movement over time\n"
            "• Used dropdown menus and buttons to improve navigation\n"
            "• Organized the interface, API calls, and data into separate files\n"
            "• Used Git and GitHub to manage project updates\n\n"
            "This project taught me how to work with external data, organize "
            "a larger Python application, and troubleshoot problems involving "
            "API requests and user interfaces."
        )

    @staticmethod
    def anton_text():
        return (
            "## Anton / Bapa Assistant\n"
            "Python Developer | 2026–Present\n\n"
            "This project began as a simple way to practice Python outside of "
            "school. Over time, it became a personal terminal assistant with "
            "commands for working with files, folders, programs, and basic "
            "computer information.\n\n"
            "## Features\n"
            "• Opens applications such as Finder, Notes, and Terminal\n"
            "• Lists files inside folders\n"
            "• Reads text files\n"
            "• Opens files and folders\n"
            "• Launches Python programs\n"
            "• Displays battery information\n"
            "• Checks disk space and Wi-Fi status\n"
            "• Handles invalid commands without immediately crashing\n\n"
            "Building Anton helped me become more comfortable with command "
            "processing, file operations, error handling, and working with "
            "the macOS operating system through Python."
        )

    @staticmethod
    def data_manager_text():
        return (
            "## Personal Data Management System\n"
            "Python and Tkinter Project\n\n"
            "I built this project to turn a basic command-line data program "
            "into a desktop application that is easier to understand and use.\n\n"
            "The application allows a user to create and manage profile "
            "information through a Tkinter interface instead of typing every "
            "command into the terminal.\n\n"
            "## Features\n"
            "• Add new profiles\n"
            "• View saved profiles\n"
            "• Search for a profile by ID\n"
            "• Update existing information\n"
            "• Delete profiles\n"
            "• Save information between sessions\n"
            "• Use radio buttons to select different actions or options\n"
            "• Enter information through text fields\n"
            "• Display success and error messages\n"
            "• Validate input before saving it\n\n"
            "This project helped me understand how the same programming logic "
            "can be used in both command-line and graphical applications."
        )

    @staticmethod
    def leadership_text():
        return (
            "## Brazilian Jiu-Jitsu\n"
            "Purple Belt Practitioner | San Diego, California\n\n"
            "I've trained in Brazilian Jiu-Jitsu for several years. Reaching "
            "purple belt required consistency, patience, and the willingness "
            "to keep learning even when progress felt slow.\n\n"
            "Training has taught me how to stay calm while solving problems, "
            "accept feedback, work with different personalities, and adjust "
            "when something is not working.\n\n"
            "## Skills Developed Through Training\n"
            "• Discipline and long-term commitment\n"
            "• Teamwork and communication\n"
            "• Problem-solving under pressure\n"
            "• Adaptability\n"
            "• Patience during difficult situations\n"
            "• Comfort with learning through failure and repetition"
        )


def main():
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
