# ==============================================================================
# Dockerfile for AI Room Cleaner Home Assistant Add-on
# ==============================================================================

# --- Build Stage 1: Frontend ---
# We will add this stage later when we develop the frontend.
# For now, we will create a placeholder index.html.

# --- Build Stage 2: Final Image ---
ARG BUILD_FROM
FROM ${BUILD_FROM}

# Set up the working directory
WORKDIR /app

# Copy the backend application code
COPY app/ /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the run script and make it executable
COPY run.sh /
RUN chmod +x /run.sh

# Expose the port for the web interface
EXPOSE 8000

# Set the entrypoint
CMD [ "/run.sh" ]