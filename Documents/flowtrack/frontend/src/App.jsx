import axios from "axios";
import { useEffect, useState } from "react";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import "./index.css";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

function ProtectedRoute({ children }) {
  const token = localStorage.getItem("access");
  return token ? children : <Navigate to="/login" />;
}

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    const res = await axios.post("http://127.0.0.1:8000/api/token/", {
      username,
      password,
    });
    localStorage.setItem("access", res.data.access);
    localStorage.setItem("refresh", res.data.refresh);
    window.location.href = "/";
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded-xl shadow w-96">
        <h2 className="text-xl font-bold mb-4">Login</h2>
        <input
          className="border p-2 w-full mb-2"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          className="border p-2 w-full mb-4"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          onClick={login}
          className="bg-blue-600 text-white w-full py-2 rounded"
        >
          Login
        </button>
      </div>
    </div>
  );
}

function Dashboard() {
  const [projects, setProjects] = useState([]);
  const [workflows, setWorkflows] = useState([]);
  const [tasks, setTasks] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);
  const [selectedWorkflow, setSelectedWorkflow] = useState(null);
  const [search, setSearch] = useState("");
  const [status, setStatus] = useState("");

  useEffect(() => {
    api.get("/projects/").then((res) => setProjects(res.data.results || res.data));
  }, []);

  useEffect(() => {
    if (selectedProject) {
      api.get(`/workflows/?project=${selectedProject}`).then((res) => setWorkflows(res.data.results || res.data));
    }
  }, [selectedProject]);

  useEffect(() => {
    if (selectedWorkflow) {
      let url = `/tasks/?workflow=${selectedWorkflow}`;
      if (search) url += `&search=${search}`;
      if (status) url += `&status=${status}`;
      api.get(url).then((res) => setTasks(res.data.results || res.data));
    }
  }, [selectedWorkflow, search, status]);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6">FlowTrack</h1>
      <div className="grid grid-cols-3 gap-6">
        <div className="bg-white p-4 rounded-xl shadow">
          <h2 className="font-semibold mb-2">Projects</h2>
          {projects.map((p) => (
            <div
              key={p.id}
              onClick={() => setSelectedProject(p.id)}
              className={`p-2 cursor-pointer rounded ${selectedProject === p.id ? "bg-blue-100" : "hover:bg-gray-100"}`}
            >
              {p.name}
            </div>
          ))}
        </div>
        <div className="bg-white p-4 rounded-xl shadow">
          <h2 className="font-semibold mb-2">Workflows</h2>
          {workflows.map((w) => (
            <div
              key={w.id}
              onClick={() => setSelectedWorkflow(w.id)}
              className={`p-2 cursor-pointer rounded ${selectedWorkflow === w.id ? "bg-green-100" : "hover:bg-gray-100"}`}
            >
              {w.name}
            </div>
          ))}
        </div>
        <div className="bg-white p-4 rounded-xl shadow">
          <h2 className="font-semibold mb-2">Tasks</h2>
          <div className="flex gap-2 mb-3">
            <input
              placeholder="Search"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="border p-2 rounded w-full"
            />
            <select
              value={status}
              onChange={(e) => setStatus(e.target.value)}
              className="border p-2 rounded"
            >
              <option value="">All</option>
              <option value="todo">Todo</option>
              <option value="doing">Doing</option>
              <option value="done">Done</option>
            </select>
          </div>
          {tasks.map((t) => (
            <div key={t.id} className="border rounded p-3 mb-2">
              <div className="font-medium">{t.title}</div>
              <div className="text-sm text-gray-500">{t.description}</div>
              <span className="text-xs bg-gray-200 rounded px-2 py-1">{t.status}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
