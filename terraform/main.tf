provider "google" {
  project = var.project
  region  = var.region
}

resource "google_pubsub_topic" "my_topic" {
  name = var.pubsub_topic_name
}
