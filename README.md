# Project: Deploying an OCR Engine with REST API and Docker

## Overview

This project involves deploying a recent OCR engine and exposing its service as a REST API. It also includes setting up a task queue to manage several workers and handle long-running, CPU-bound tasks. The project is divided into multiple stages, each with specific deliverables, acceptance conditions, and grading points.

## Stage 1: Dockerized Minimal Web App

### Objective
- Deploy a minimal web app using Docker with a production-ready server.

## Stage 2: Fake Image Processing Service

### Objective
- Add a new route `/imgshape/` to the previous application, which accepts image uploads and returns a JSON response with the shape of the image.

## Stage 3: Dockerized OCR System

### Objective
- Create a Docker image where the OCR processes all input images available under `/data/input/*.jpg` and writes the corresponding outputs to `/data/output/`.

## Stage 4: Dockerized OCR System Exposed Over a Synchronous REST API

### Objective
- Merge stage 2 and 3 to expose the OCR functions through a REST API.


### Run

Docker compose up

