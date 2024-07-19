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
