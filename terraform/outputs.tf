output "pubsub_topic_name" {
  description = "The name of the Pub/Sub topic"
  value       = google_pubsub_topic.values.name
}
