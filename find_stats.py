import re
import matplotlib.pyplot as plt
import os

def parse_section(content):
    """Extracts task completion from a section."""
    tasks = re.findall(r'\|\s*\[(.*?)\]\(https://leetcode.com/problems/.*?\)\s*\|\s*\[(.)\]\s*\|', content)
    total = len(tasks)
    done = sum(1 for _, mark in tasks if mark.lower() == 'x')
    return done, total

def extract_sections(markdown):
    """Extract each difficulty section from the markdown text."""
    pattern = re.compile(r'### (Easy|Medium|Hard)(.*?)((?=###)|\Z)', re.S)
    return pattern.findall(markdown)

def generate_pie_chart(stats, output_path='leetcode_progress.png'):
    labels = []
    sizes = []
    for difficulty, (done, total) in stats.items():
        if total > 0:
            labels.append(f'{difficulty}')
            sizes.append(done)

    remaining = sum(total - done for done, total in stats.values())
    if remaining > 0:
        labels.append('Unsolved')
        sizes.append(remaining)

    if not sizes:
        return

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.axis('equal')
    plt.title('LeetCode Progress Distribution')
    plt.savefig(output_path)
    plt.close()

def compute_and_update_stats(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = extract_sections(content)
    stats = {}
    total_done = total_problems = 0

    for difficulty, section, _ in sections:
        done, total = parse_section(section)
        stats[difficulty] = (done, total)
        total_done += done
        total_problems += total

    # Generate and save the chart
    generate_pie_chart(stats)

    print("Chart generated and markdown updated with progress image.")

# Example usage:
compute_and_update_stats('README.md'.lower())
