
"""
Program: Resume_App.py
Author: Pedro Ledezma
"""

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
            "Phishing Detector": self.phishing_text(),
            "Interactive Resume": self.resume_text(),
            "Data Structures": self.data_structures_text(),
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
            text="Software Development | IT Support | Linux | Cybersecurity",
            font=("Arial", 13),
            bg="#172033",
            fg="#cbd5e1",
        )
        title_label.pack()

        contact_label = tk.Label(
            header,
            text="San Diego, CA   •   garciarexx33@gmail.com",
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

        separator = tk.Frame(
            navigation,
            bg="#e2e8f0",
            height=1,
        )
        separator.pack(fill="x", padx=20, pady=18)

        # Use clickable Labels instead of native Tk buttons
        # to keep text and background colors consistent on macOS.
        self.make_action_button(
            navigation,
            "Open GitHub",
            self.open_github,
            "#2563eb",
            "#ffffff",
        )

        self.make_action_button(
            navigation,
            "Send Email",
            self.send_email,
            "#475569",
            "#ffffff",
        )

        self.make_action_button(
            navigation,
            "Copy Current Section",
            self.copy_section,
            "#e2e8f0",
            "#172033",
        )

    def make_action_button(
        self, parent, text, command, bg, fg
    ):
        button = tk.Label(
            parent,
            text=text,
            font=("Arial", 10, "bold"),
            bg=bg,
            fg=fg,
            cursor="hand2",
            pady=12,
            relief="flat",
        )
        button.pack(fill="x", padx=20, pady=(0, 10))

        button.bind("<Button-1>", lambda event: command())

        # Keyboard accessibility
        button.configure(takefocus=1)
        button.bind("<Return>", lambda event: command())
        button.bind("<space>", lambda event: command())

        original_bg = bg

        def on_enter(event):
            if bg == "#2563eb":
                button.config(bg="#1d4ed8")
            elif bg == "#475569":
                button.config(bg="#334155")
            else:
                button.config(bg="#cbd5e1")

        def on_leave(event):
            button.config(bg=original_bg)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def create_content_area(self, parent):
        content_card = tk.Frame(
            parent,
            bg="#ffffff",
            highlightthickness=1,
            highlightbackground="#d7dce2",
        )
        content_card.pack(
            side="right",
            fill="both",
            expand=True,
        )

        self.section_title = tk.Label(
            content_card,
            text="",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#172033",
            anchor="w",
        )
        self.section_title.pack(
            fill="x",
            padx=35,
            pady=(30, 10),
        )

        title_line = tk.Frame(
            content_card,
            bg="#2563eb",
            height=3,
        )
        title_line.pack(
            fill="x",
            padx=35,
            pady=(0, 20),
        )

        text_container = tk.Frame(
            content_card,
            bg="#ffffff",
        )
        text_container.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25),
        )

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
        self.content_text.pack(
            side="left",
            fill="both",
            expand=True,
        )

        scrollbar.config(
            command=self.content_text.yview
        )

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
        webbrowser.open(
            "https://github.com/garciarexx33-bit"
        )

    @staticmethod
    def send_email():
        webbrowser.open(
            "mailto:garciarexx33@gmail.com"
        )

    @staticmethod
    def about_me_text():
        return (
            "## Professional Profile\n"
            "Computer Science student at San Diego Mesa College "
            "with hands-on experience in software development, "
            "operating systems, and technical troubleshooting. "
            "My work spans Python, C++, Java, Linux, and desktop "
            "application development.\n\n"

            "## Technical Focus\n"
            "I build interactive applications, integrate external "
            "APIs, implement data structures and algorithms, and "
            "work with Linux command-line tools. I use Git and "
            "GitHub to manage source code and track development "
            "changes.\n\n"

            "My projects include a live MMA odds tracker, a Python "
            "phishing detection tool, and an interactive resume "
            "application. I also have practical experience "
            "configuring operating systems and diagnosing hardware "
            "and software issues.\n\n"

            "## Career Interests\n"
            "I am pursuing opportunities in IT support, help desk, "
            "software development, and cybersecurity. I value "
            "clear communication, methodical troubleshooting, "
            "and reliable solutions."
        )

    @staticmethod
    def education_text():
        return (
            "## San Diego Mesa College\n"
            "San Diego, California\n"
            "Associate Degree in Computer Science — In Progress\n\n"

            "## Relevant Coursework\n"
            "• Data Structures and Algorithms (C++)\n"
            "• Object-Oriented Programming (C++ and Java)\n"
            "• Python Programming\n"
            "• Discrete Mathematics\n"
            "• Linux and Computer Systems\n"
            "• SQL and Database Fundamentals\n"
            "• Trigonometry\n\n"

            "## Applied Learning\n"
            "• Implemented classes, inheritance, pointers, "
            "trees, and sorting algorithms\n"
            "• Built and tested C++ programs in a Linux environment\n"
            "• Used Git, CMake, and automated tests for "
            "coursework projects"
        )

    @staticmethod
    def skills_text():
        return (
            "## IT Support and Systems\n"
            "• Hardware and software troubleshooting\n"
            "• Linux command-line operations and system configuration\n"
            "• Operating system installation and setup\n"
            "• Shell scripting and file management\n"
            "• Technical problem diagnosis\n\n"

            "## Programming and Development\n"
            "• Python, C++, Java\n"
            "• SQL fundamentals\n"
            "• Data structures and algorithms\n"
            "• Object-oriented programming\n"
            "• Tkinter desktop GUI development\n"
            "• REST API integration and JSON\n"
            "• File I/O, error handling, and input validation\n\n"

            "## Development Tools\n"
            "• Git and GitHub\n"
            "• Visual Studio Code and IDLE\n"
            "• CMake and automated testing\n"
            "• Linux terminal and command-line utilities\n\n"

            "## Cybersecurity\n"
            "• Phishing indicator analysis\n"
            "• Rule-based email risk scoring\n"
            "• Security fundamentals and threat awareness"
        )

    @staticmethod
    def fightline_text():
        return (
            "## FightLine — UFC Odds Tracker\n"
            "Python | Tkinter | The Odds API\n\n"

            "Developed a desktop application that retrieves "
            "and displays MMA betting odds from multiple sportsbooks.\n\n"

            "## Features\n"
            "• Integrated The Odds API for sportsbook data\n"
            "• Implemented automatic odds refresh\n"
            "• Tracked betting-line movement\n"
            "• Organized data in an interactive Tkinter interface\n"
            "• Used Git and GitHub for version control\n\n"

            "## Repository\n"
            "https://github.com/garciarexx33-bit/fight-line"
        )

    @staticmethod
    def phishing_text():
        return (
            "## Phishing Detector\n"
            "Python | Cybersecurity | Rule-Based Analysis\n\n"

            "Developed a Python tool that evaluates email content "
            "for potential phishing indicators and generates an "
            "explainable risk assessment.\n\n"

            "## Features\n"
            "• Checks for suspicious keywords and urgency tactics\n"
            "• Examines URLs and potentially risky domain patterns\n"
            "• Flags credential requests and unusual payment instructions\n"
            "• Uses weighted indicators to classify risk levels\n"
            "• Provides warnings explaining detected concerns\n\n"

            "## Repository\n"
            "https://github.com/garciarexx33-bit/phishing-detector"
        )

    @staticmethod
    def resume_text():
        return (
            "## Interactive Resume Application\n"
            "Python | Tkinter | Desktop GUI\n\n"

            "Developed this interactive desktop resume to present "
            "my technical background, education, and projects "
            "through a navigable graphical interface.\n\n"

            "## Features\n"
            "• Section-based navigation with radio buttons\n"
            "• Scrollable, formatted resume content\n"
            "• GitHub and email actions\n"
            "• One-click copying of resume sections\n"
            "• Responsive window sizing and organized layout\n\n"

            "## Repository\n"
            "https://github.com/garciarexx33-bit/interactive-resume-app"
        )

    @staticmethod
    def data_structures_text():
        return (
            "## C++ Data Structures and Algorithms\n"
            "C++ | Linux | Git | CMake\n\n"

            "Completed hands-on implementations and tests "
            "covering core data structures, object-oriented "
            "design, and algorithm behavior.\n\n"

            "## Topics and Implementations\n"
            "• Trees and preorder, inorder, postorder, "
            "and level-order traversals\n"
            "• Sorting algorithm analysis and comparison\n"
            "• Lists, classes, constructors, and operator overloading\n"
            "• Inheritance, polymorphism, and pointer-based objects\n"
            "• Automated builds and tests using CMake and CTest\n"
            "• Memory-checking workflows with Valgrind\n\n"

            "Coursework repository available upon request "
            "if access is restricted."
        )

    @staticmethod
    def anton_text():
        return (
            "## Anton — Python Assistant\n"
            "Python | macOS | Command-Line Utilities\n\n"

            "Developed a command-driven assistant for working "
            "with files, folders, applications, and basic "
            "system information.\n\n"

            "## Technical Work\n"
            "• Processed user commands and handled invalid input\n"
            "• Implemented file and directory operations\n"
            "• Launched applications and Python programs\n"
            "• Retrieved basic system status information\n\n"

            "## Repository\n"
            "https://github.com/garciarexx33-bit/anton-python-assistant\n\n"

            "## Bapa — Python Assistant\n"
            "Created a separate experimental text-command "
            "assistant project.\n"
            "https://github.com/garciarexx33-bit/bapa-py"
        )

    @staticmethod
    def data_manager_text():
        return (
            "## Personal Data Management System\n"
            "Python | Tkinter\n\n"

            "Built a desktop interface for creating and "
            "maintaining saved profile records.\n\n"

            "## Features\n"
            "• Add, view, search, update, and delete profiles\n"
            "• Save data between sessions\n"
            "• Validate user input\n"
            "• Display confirmation and error messages\n"
            "• Navigate through graphical controls\n\n"

            "This project applies CRUD operations, file "
            "persistence, and event-driven interface design."
        )

    @staticmethod
    def leadership_text():
        return (
            "## Brazilian Jiu-Jitsu\n"
            "Purple Belt | San Diego, California\n\n"

            "Years of training in Brazilian Jiu-Jitsu have "
            "strengthened my discipline, adaptability, teamwork, "
            "and ability to remain composed under pressure.\n\n"

            "## Transferable Strengths\n"
            "• Consistent practice and long-term commitment\n"
            "• Clear communication and constructive feedback\n"
            "• Analytical problem-solving under pressure\n"
            "• Adaptability and teamwork"
        )


def main():
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
