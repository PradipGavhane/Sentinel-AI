import subprocess

def auto_heal():

    containers = [
        "prometheus",
        "grafana",
        "node-exporter",
        "alertmanager"
    ]

    print("=" * 50)
    print("Sentinel AI - Auto Healing Engine")
    print("=" * 50)

    for container in containers:

        result = subprocess.run(
            ["docker", "inspect", "-f", "{{.State.Running}}", container],
            capture_output=True,
            text=True
        )

        status = result.stdout.strip()

        if status == "true":
            print(f"✅ {container} : Running")

        else:
            print(f"❌ {container} : Stopped")
            print(f"🔄 Restarting {container}...")

            restart = subprocess.run(
                ["docker", "restart", container],
                capture_output=True,
                text=True
            )

            if restart.returncode == 0:
                print(f"✅ {container} restarted successfully.")
            else:
                print(f"❌ Failed to restart {container}.")

    print("=" * 50)


if __name__ == "__main__":
    auto_heal()