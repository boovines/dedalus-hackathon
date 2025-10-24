"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Bot } from "lucide-react";

type ToolCall = { server?: string; tool?: string; input?: any; output?: any };
type Resp = { final_output?: string; tool_calls?: ToolCall[]; error?: string; detail?: string };

export default function Home() {
  const [query, setQuery] = useState("Summarize latest reporting on the shutdown timing and decide YES or NO with a one-sentence rationale. Cite sources.");
  const [isRunning, setIsRunning] = useState(false);
  const [res, setRes] = useState<Resp | null>(null);

  const handleRun = async () => {
    setIsRunning(true);
    setRes(null);
    try {
      const r = await fetch("/api/think", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      const j = await r.json();
      setRes(j);
    } finally {
      setIsRunning(false);
    }
  };

  const handleReset = () => {
    setQuery("");
    setRes(null);
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-background p-4">
      <div className="w-full max-w-3xl space-y-6">
        <div className="text-center space-y-2">
          <h1 className="text-3xl font-semibold tracking-tight">Single Agent</h1>
          <p className="text-muted-foreground">Type a prompt. The agent will think, search with Brave, and show thoughts.</p>
        </div>

        <Card className="p-8 space-y-4">
          <label htmlFor="prompt" className="text-sm font-medium">Prompt</label>
          <textarea
            id="prompt"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            rows={5}
            className="w-full rounded-md border bg-background p-3 outline-none focus:ring-2 focus:ring-ring"
            placeholder="Describe what you want the agent to do"
          />
          <div className="flex gap-3">
            <Button onClick={handleRun} disabled={isRunning || !query.trim()} className="flex-1">
              {isRunning ? "Running..." : "Run"}
            </Button>
            <Button onClick={handleReset} variant="outline">Reset</Button>
          </div>
        </Card>

        {res?.error && (
          <Card className="p-4">
            <pre className="whitespace-pre-wrap text-red-400">{JSON.stringify(res, null, 2)}</pre>
          </Card>
        )}

        {res?.final_output && (
          <Card className="p-4 space-y-2">
            <div className="flex items-center gap-2">
              <Bot className="h-4 w-4" />
              <h3 className="font-medium">Answer</h3>
            </div>
            <pre className="whitespace-pre-wrap">{res.final_output}</pre>
          </Card>
        )}

        {res?.tool_calls && (
          <Card className="p-4 space-y-2">
            <div className="flex items-center gap-2">
              <Bot className="h-4 w-4" />
              <h3 className="font-medium">Thoughts</h3>
            </div>
            <pre className="whitespace-pre-wrap text-sm">{JSON.stringify(res.tool_calls, null, 2)}</pre>
          </Card>
        )}
      </div>
    </div>
  );
}
