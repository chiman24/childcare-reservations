#Register the task definition in the repository
aws ecs register-task-definition --cli-input-json file://task-definition.json
