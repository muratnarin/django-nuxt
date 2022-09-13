export default function ({ $auth, redirect }) {
  if (!$auth.user?.is_superuser) {
    return redirect("/");
  }
}
