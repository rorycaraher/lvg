output "pubsub_topic_name" {
  description = "The name of the Pub/Sub topic"
  value       = google_pubsub_topic.level_values.name
}

output "static_site_url" {
  description = "The URL of the static site"
  value       = "http://${google_storage_bucket.static_site_bucket.name}.storage.googleapis.com"
}

output "db_instance_connection_name" {
  description = "The connection name of the Cloud SQL instance"
  value       = google_sql_database_instance.db_instance.connection_name
}

output "db_name" {
  description = "The name of the database"
  value       = google_sql_database.db.name
}

output "db_user" {
  description = "The database user"
  value       = google_sql_user.db_user.name
}

output "audio_bucket_name" {
  description = "The name of the audio storage bucket"
  value       = google_storage_bucket.audio_bucket.name
}
