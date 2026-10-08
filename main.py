#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linux Command Finder
---------------------
Oyaa monawada karanna one kiyala simple widihata liwuwahama,
gälapena Linux command eka pennana simple GUI app ekak.

Run karanna:  python3 main.py
Awashya krama: Python 3 witharai (tkinter Python ekka ekka enawa).
"""

import tkinter as tk
from tkinter import ttk
import difflib

from commands_db import COMMANDS

# ---------------------------------------------------------------------------
# Colors / Theme
# ---------------------------------------------------------------------------
BG = "#0f172a"          # dark navy background
CARD_BG = "#1e293b"     # slightly lighter card background
ACCENT = "#22d3ee"      # cyan accent
ACCENT_2 = "#38bdf8"
TEXT_MAIN = "#e2e8f0"
TEXT_MUTED = "#94a3b8"
ENTRY_BG = "#1e293b"
BORDER = "#334155"


def score_entry(query_words, entry):
    """Query eke words tika, command entry ekaka keywords/description/command
    tika ekka compare karala match score ekak denawa."""
    haystack = " ".join(entry["keywords"]) + " " + entry["description"] + " " + entry["command"]
    haystack = haystack.lower()

    score = 0
    for w in query_words:
        if not w:
            continue
        if w in haystack:
            score += 3
        else:
            # fuzzy match - typo tikak thibbath match wenna
            close = difflib.get_close_matches(w, haystack.split(), n=1, cutoff=0.8)
            if close:
                score += 1
    return score


def search_commands(query, limit=8):
    query = query.strip().lower()
    if not query:
        return []
    query_words = query.replace(",", " ").split()

    results = []
    for entry in COMMANDS:
        s = score_entry(query_words, entry)
        if s > 0:
            results.append((s, entry))

    results.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in results[:limit]]


class ResultCard(ttk.Frame):
    """Result ekak pennana card widget eka (command + description + copy button)."""

    def __init__(self, parent, command_text, description_text, on_copy):
        super().__init__(parent, style="Card.TFrame", padding=14)

        desc_label = tk.Label(
            self,
            text=description_text,
            bg=CARD_BG,
            fg=TEXT_MUTED,
            font=("Segoe UI", 10),
            anchor="w",
            justify="left",
            wraplength=560,
        )
        desc_label.pack(fill="x", pady=(0, 6))

        row = tk.Frame(self, bg=CARD_BG)
        row.pack(fill="x")

        cmd_label = tk.Label(
            row,
            text=command_text,
            bg="#0b1220",
            fg=ACCENT,
            font=("Consolas", 12, "bold"),
            anchor="w",
            padx=10,
            pady=8,
        )
        cmd_label.pack(side="left", fill="x", expand=True)

        copy_btn = tk.Button(
            row,
            text="Copy",
            command=lambda: on_copy(command_text),
            bg=ACCENT,
            fg="#0b1220",
            activebackground=ACCENT_2,
            activeforeground="#0b1220",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=14,
            pady=6,
            cursor="hand2",
        )
        copy_btn.pack(side="right", padx=(10, 0))


class LinuxCommandFinderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Linux Command Finder")
        self.geometry("720x600")
        self.minsize(600, 480)
        self.configure(bg=BG)

        self._setup_style()
        self._build_ui()

    # ------------------------------------------------------------------
    def _setup_style(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("TFrame", background=BG)
        style.configure("Card.TFrame", background=CARD_BG, relief="flat")

        style.configure(
            "Search.TEntry",
            fieldbackground=ENTRY_BG,
            background=ENTRY_BG,
            foreground=TEXT_MAIN,
            insertcolor=TEXT_MAIN,
            bordercolor=BORDER,
            lightcolor=BORDER,
            darkcolor=BORDER,
            padding=10,
        )

    # ------------------------------------------------------------------
    def _build_ui(self):
        # ---------- Header ----------
        header = tk.Frame(self, bg=BG)
        header.pack(fill="x", padx=24, pady=(24, 12))

        title = tk.Label(
            header,
            text="🐧 Linux Command Finder",
            bg=BG,
            fg=TEXT_MAIN,
            font=("Segoe UI", 20, "bold"),
        )
        title.pack(anchor="w")

        subtitle = tk.Label(
            header,
            text="Monawada karanna one kiyala liyanna — ona Linux command eka mehema pennanawa.",
            bg=BG,
            fg=TEXT_MUTED,
            font=("Segoe UI", 10),
        )
        subtitle.pack(anchor="w", pady=(4, 0))

        # ---------- Search box ----------
        search_frame = tk.Frame(self, bg=BG)
        search_frame.pack(fill="x", padx=24, pady=(4, 12))

        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            bg=ENTRY_BG,
            fg=TEXT_MAIN,
            insertbackground=TEXT_MAIN,
            relief="flat",
            font=("Segoe UI", 13),
            highlightthickness=2,
            highlightbackground=BORDER,
            highlightcolor=ACCENT,
        )
        self.search_entry.pack(side="left", fill="x", expand=True, ipady=10, padx=(0, 10))
        self.search_entry.insert(0, "e.g. file ekak delete karanna one / disk space balanna")
        self.search_entry.config(fg=TEXT_MUTED)
        self.search_entry.bind("<FocusIn>", self._clear_placeholder)
        self.search_entry.bind("<KeyRelease>", self._on_type)

        search_btn = tk.Button(
            search_frame,
            text="Search",
            command=self._on_search,
            bg=ACCENT,
            fg="#0b1220",
            activebackground=ACCENT_2,
            activeforeground="#0b1220",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            padx=20,
            cursor="hand2",
        )
        search_btn.pack(side="left", ipady=8)

        # ---------- Status ----------
        self.status_var = tk.StringVar(value="Search karanna wachanayak type karanna uda pena thiyena box eke.")
        status_label = tk.Label(
            self, textvariable=self.status_var, bg=BG, fg=TEXT_MUTED, font=("Segoe UI", 9)
        )
        status_label.pack(fill="x", padx=26, anchor="w")

        # ---------- Results (scrollable) ----------
        results_container = tk.Frame(self, bg=BG)
        results_container.pack(fill="both", expand=True, padx=24, pady=(12, 24))

        canvas = tk.Canvas(results_container, bg=BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(results_container, orient="vertical", command=canvas.yview)
        self.results_frame = tk.Frame(canvas, bg=BG)

        self.results_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.results_frame, anchor="nw", width=660)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # mouse wheel scroll
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self._show_empty_state()

    # ------------------------------------------------------------------
    def _clear_placeholder(self, event=None):
        if self.search_entry.get().startswith("e.g."):
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg=TEXT_MAIN)

    def _on_type(self, event=None):
        if event and event.keysym == "Return":
            self._on_search()

    def _clear_results(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

    def _show_empty_state(self):
        self._clear_results()
        empty = tk.Label(
            self.results_frame,
            text="Results mehe pennanne 👇\n\nUdanla search box eke tamange kaarayak\nSinhala/Singlish/English walin liyanna.",
            bg=BG,
            fg=TEXT_MUTED,
            font=("Segoe UI", 11),
            justify="center",
        )
        empty.pack(pady=60)

    def _on_search(self):
        query = self.search_var.get()
        if query.startswith("e.g."):
            return

        results = search_commands(query)
        self._clear_results()

        if not results:
            self.status_var.set("Kisima matching command ekak hambuna nehe. Wena widihakata liyala balanna.")
            no_res = tk.Label(
                self.results_frame,
                text="😕 Kisima command ekak hambuna nehe.\nTry karanna wena wachana walin (e.g. 'file delete', 'disk space', 'install package').",
                bg=BG,
                fg=TEXT_MUTED,
                font=("Segoe UI", 11),
                justify="center",
            )
            no_res.pack(pady=60)
            return

        self.status_var.set(f"{len(results)} commands hambuna.")

        for entry in results:
            card = ResultCard(
                self.results_frame,
                entry["command"],
                entry["description"],
                self._copy_to_clipboard,
            )
            card.pack(fill="x", pady=6)

    def _copy_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        self.status_var.set(f"Copy una: {text}")


if __name__ == "__main__":
    app = LinuxCommandFinderApp()
    app.mainloop()
