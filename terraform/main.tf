data "google_project" "project" {
  project_id = var.project
}

provider "google" {
  project = data.google_project.project.project_id
  region  = var.region
}

resource "google_pubsub_topic" "level_values" {
  name = var.pubsub_topic_name
}

resource "google_storage_bucket" "audio_bucket" {
  name     = "${var.project}-audio-bucket"
  location = var.region
  force_destroy = true
}
