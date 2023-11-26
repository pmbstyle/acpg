# AI Color Scheme Generator

![Demo](https://csg.trofimov.ca/preview.png)

## Live

https://csg.trofimov.ca

## Overview
The AI Color Scheme Generator is a web application that allows users to upload images and generate color palettes based on those images. It showcases the integration of Vue.js frontend with a Flask backend, along with the use of AI to analyze images and extract dominant colors.

## Features
- Upload images to generate color schemes.
- View and copy the RGB values of generated colors.
- Responsive and modern UI with Tailwind CSS and DaisyUI.
- Dockerized setup for easy deployment and development.

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js (for local development)

### Installation and Setup
1. **Clone the Repository:**
   `git clone https://github.com/pmbstyle/acpg.git`
   `cd acpg`
   
2. **Build and Run the Docker Containers:**
   `docker-compose up --build`
   
This will start the frontend accessible on http://localhost:8088 and the backend on http://localhost:5000.

### Usage
1. Navigate to http://localhost:8088 in your web browser.
2. Upload an image to generate a color palette.
3. Click on any color in the generated palette to copy its RGB value to the clipboard.

## Acknowledgments
1. Color Thief Python library for color extraction.
2. Vue.js and Tailwind CSS for building the frontend.
3. Flask for creating the backend API.
4. Docker and Docker Compose for containerization and easy deployment.