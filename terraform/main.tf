
provider "google" {
  project = var.project
  region  = var.region
}

resource "google_pubsub_topic" "my_topic" {
  name = var.pubsub_topic_name
}

output "debug_project" {
  value = var.project
}

output "debug_region" {
  value = var.region
}

output "pubsub_topic_name" {
  value = google_pubsub_topic.my_topic.name
}
