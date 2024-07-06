# Telegram Data Scraping and Analysis Using Telethon and Flask

## Project Overview

We are pleased to share our team's recent project at Université Internationale de Rabat: the development of an advanced bot using the Telethon library for Telegram data scraping and analysis. This tool provides detailed insights into user behavior and communication patterns, supporting academic research, cybersecurity, and market analysis. By systematically collecting and processing large volumes of data, this bot offers valuable resources for exploring digital communication trends and understanding online social behaviors.

Team Members

    Adam Habibi
    Abdelfattah Hanafi
    Sohaib Belhassan

## Features

- Scrapes data from specified Telegram channels
- Analyzes user interactions and communication patterns
- Provides valuable insights for research and practical applications
- Stores data in a CSV file with details on channel, sender, date, message, and media

## Requirements

- Python 3.7+
- Telethon library
- Flask framework
- SQLite for data storage

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telegram-data-scraping.git
   ```
2. Navigate to the project directory:
   ```bash
   cd telegram-data-scraping
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up your Telegram API credentials by creating a `config.py` file and adding your `api_id` and `api_hash`:
   ```python
   api_id = 'your_api_id'
   api_hash = 'your_api_hash'
   phone_number = '+xxx xxxxxxxxxxxxxxx'
   ```
2. Run the Telegram scraper bot:
   ```bash
   python scraper.py
   ```
3. Start the Flask web application:
   ```bash
   python app.py
   ```
Here is a screenshot of the graphical interface:

![Screenshot 2024-07-06 202912](https://github.com/abdouhanafi/telegram-data-scraping/assets/95773668/556b2e10-ae9f-425e-ae26-ec38d9065098)



## Legal Notice

### Purpose and Limitations of Use

This document pertains to an academic project titled "Telegram Data Scraping and Analysis Using Telethon and Flask," conducted under the supervision of Prof. Othmane Cherqi and Prof. Anass Sebbar at Université Internationale de Rabat during the 2024 academic year. The authors of this project, Adam Habibi, Abdelfattah Hanafi, and Sohaib Belhassan, have undertaken this study strictly for educational and research purposes.

The methodologies, tools, algorithms, and technologies discussed and employed within this project are designed solely to explore and enhance understanding of data collection practices and to develop capabilities in data analysis within an academic framework. This project does not advocate for, nor supports, the deployment of these techniques in environments where they might contravene privacy rights, legal stipulations, or ethical standards.

### Intellectual Property and Usage Rights

All intellectual property generated from this project, including code, methodologies, documentation, and findings, are the property of the authors and the associated institution unless otherwise noted, with all rights reserved. Usage of any material from this project without proper authorization or beyond the scope of academic and educational purposes is strictly prohibited.

### Accuracy and Reliability of Information

While every effort has been made to ensure the accuracy and reliability of the information presented in this report, the authors and the associated institution make no representation or warranties, either expressed or implied, as to the precision, reliability, or completeness of the information. The methodologies and results presented are based on the conditions and data available during the course of the research and are subject to change in response to new data or further analysis.

### Indemnity

The authors and the associated institution shall not be held liable for any losses, damages, costs, or expenses arising from the use of, or reliance on, the information contained within this project, including any indirect or consequential losses or damages. Users of the information from this project do so at their own risk and are responsible for ensuring that any applications of this information are compliant with all relevant laws and regulations.

### Compliance with Ethical Standards

This project has been conducted in accordance with the ethical guidelines laid out by our academic institution, which include respecting privacy norms and ensuring data security. Any data collection from Telegram channels was performed in a controlled environment, and any personal data obtained was anonymized and used strictly within the bounds of academic research.

## Conclusion

This project effectively demonstrates how the Telethon, Flask, and SQLite libraries can be integrated to develop a robust system for scraping, storing, and analyzing data from Telegram channels. The benefits of this project extend beyond its immediate functionality, serving as a powerful tool in fields like market research, social media analysis, and cybersecurity, offering insights that can inform strategies and decision-making processes.

By continuously improving and expanding this project, such as incorporating machine learning and real-time data analysis, we aim to enhance our understanding of digital communication landscapes further.

