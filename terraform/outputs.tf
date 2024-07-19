output "pubsub_topic_name" {
  description = "The name of the Pub/Sub topic"
  value       = google_pubsub_topic.level_values.name
}

output "audio_bucket_name" {
  description = "The name of the audio storage bucket"
  value       = google_storage_bucket.audio_bucket.name
}
