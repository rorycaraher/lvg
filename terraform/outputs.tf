output "project" {
  description = "The GCP project in use"
  value       = var.project
}

output "pubsub_topic_name" {
  description = "The name of the Pub/Sub topic"
  value       = google_pubsub_topic.my_topic.name
}

output "region" {
  description = "The GCP region in use"
  value       = var.region
}
