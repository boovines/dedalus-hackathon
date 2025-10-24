import { NextRequest, NextResponse } from 'next/server';
import { spawn } from 'node:child_process';
import path from 'node:path';

export async function POST(req: NextRequest) {
  const { query } = await req.json().catch(() => ({ query: '' }));
  const script = path.join(process.cwd(), 'agents', 'market_agent.py');

  return new Promise((resolve) => {
    const args = ['run', '--with', 'dedalus-labs', '--with', 'python-dotenv', script];
    if (query) args.push(String(query));

    const child = spawn('uv', args, { env: { ...process.env } });

    let out = '', err = '';
    child.stdout.on('data', d => out += d.toString());
    child.stderr.on('data', d => err += d.toString());

    child.on('close', (code) => {
      if (code === 0) {
        try { resolve(NextResponse.json(JSON.parse(out))); }
        catch { resolve(NextResponse.json({ final_output: out.trim(), tool_calls: null }, { status: 200 })); }
      } else {
        resolve(NextResponse.json({ error: 'runner failed', detail: err || out }, { status: 500 }));
      }
    });
  });
}
