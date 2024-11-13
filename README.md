# My Browser Indexing System

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)  
An information retrieval and indexing tool for efficient document management and fast keyword-based searches.

## Table of Contents
- [Introduction](#introduction)
- [Goal](#goal)
- [Document Collection](#document-collection)
- [Implementation](#implementation)
- [Approaches](#approaches)
- [Backend Functionality](#backend-functionality)
- [User Interface](#user-interface)
- [Shortcomings](#shortcomings)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)

---

## Introduction
This project implements an indexing system to efficiently organize and retrieve data from text documents. The indexing process enables fast search and retrieval by recording terms, frequencies, and positions within documents. It’s designed for applications such as search engines and document management systems.

## Goal
The primary objective is to build an indexing system supporting document retrieval by both name and content. The system enables quick keyword-based searches within content and file identification by name, improving search accuracy and speed for large document collections.

## Document Collection
This project indexes a folder of `.txt` files, each containing text sourced from Wikipedia on various topics. Example documents include:
- Science
- Plants
- Animals
- Computer
- AI
- Pokemon

## Implementation
Implemented in Python, the indexing system processes text files without any external libraries. Key features include:
1. **Index Creation**: Reads and indexes documents while filtering out stop words and normalizing words to base forms by removing prefixes and suffixes.
2. **Search Options**:
   - **By Document Name**: Allows users to locate and open files by name.
   - **By Content**: Supports keyword-based searches across document content.
3. **Update and Refresh**: Provides a manual refresh option to re-index files if they’re modified or new files are added.

## Approaches

### Initial Approach
- **Goal**: Capture all possible keywords by indexing every word.
- **Result**: Produced excessive, redundant data with minimal relevance.

### Current Approach
- **Goal**: Refine indexing to focus on relevant terms.
- **Solution**: Introduced stop words (e.g., "is," "am," "are") and lists of verb and noun suffixes to filter and normalize data.
- **Result**: Improved relevance of index while reducing redundancy.

## Backend Functionality

### 1. Index Creation
- **Stop Words**: Words are checked against an external stop words list.
- **Prefix and Suffix Removal**: Uses files of prefixes and suffixes to obtain base forms of words.
- **Punctuation Removal**: Custom function removes specific punctuation (e.g., `.`, `,`, `?`, `!`) for consistency.
- **Indexing**: Stores normalized words with frequency and line occurrences.

### 2. Search by Document
Allows users to search by document name, opening the file’s location if found.

### 3. Search by Content
Keyword-based searches return documents containing query words, showing the frequency and line numbers of occurrences.

## User Interface

### Home Screen
The main menu displays:
1. **Refresh Indexer Manually**: Refreshes to include new or modified files.
2. **Search by Document Name**: Finds and opens a file by its name.
3. **Search by Document Content**: Enables keyword-based content search.
4. **Exit**: Closes the program.

## Shortcomings
- **Manual Refresh**: Requires manual index refresh; could benefit from automated detection of file changes.
- **List Management**: Extensive prefix and suffix lists may affect performance.
- **Limited Punctuation Handling**: Only specific punctuation marks are removed.
- **No Spell Correction**: Currently lacks typo or spelling variation handling.

## Usage
1. **Run the main script**:
    ```bash
    python index.py
    ```
2. **Choose from the Menu**:
    - **Refresh Indexer**: Manually updates indexes for new or modified files.
    - **Search by Document Name**: Allows file retrieval by name.
    - **Search by Document Content**: Enter keywords to search indexed content.
    - **Exit**: Exits the program.
