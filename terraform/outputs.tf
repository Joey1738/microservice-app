output "namespace" {
  value = kubernetes_namespace.dev.metadata[0].name
}
