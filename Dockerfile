FROM python:3.12-slim

WORKDIR /app
COPY . .

# Make sure this build's key opens the drafts vault, then keep the vault out of the image.
ARG NEST_KEY
RUN python -m paper_nest vault check .nest/drafts.vault && rm -rf .nest

ENV PYTHONPATH=/app
WORKDIR /site
ENTRYPOINT ["python", "-m", "paper_nest"]
CMD ["build"]
