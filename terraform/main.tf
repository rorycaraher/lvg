provider "google" {
  project = var.project
  region  = var.region
}

resource "google_pubsub_topic" "level_values" {
  name = var.pubsub_topic_name
}
