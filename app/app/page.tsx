"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Upload, Image as ImageIcon } from "lucide-react";

export default function Home() {
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setSelectedImage(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);

    const file = e.dataTransfer.files?.[0];
    if (file && file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setSelectedImage(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleAnalyze = async () => {
    setIsAnalyzing(true);
    // AI analysis will be implemented here
    setTimeout(() => {
      setIsAnalyzing(false);
    }, 2000);
  };

  const handleReset = () => {
    setSelectedImage(null);
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-background p-4">
      <div className="w-full max-w-2xl space-y-6">
        <div className="text-center space-y-2">
          <h1 className="text-3xl font-semibold tracking-tight">
            Bet Analyzer
          </h1>
          <p className="text-muted-foreground">
            Upload your bet slip or parlay for AI-powered analysis
          </p>
        </div>

        <Card className="p-8 space-y-6">
          {!selectedImage ? (
            <div
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              onDrop={handleDrop}
              className={`border-2 border-dashed rounded-lg p-12 text-center transition-colors ${
                isDragging
                  ? "border-foreground bg-muted"
                  : "border-muted-foreground/25 hover:border-muted-foreground/50"
              }`}
            >
              <div className="flex flex-col items-center gap-4">
                <div className="rounded-full bg-muted p-4">
                  <Upload className="h-8 w-8 text-muted-foreground" />
                </div>
                <div className="space-y-2">
                  <p className="text-lg font-medium">
                    Drop your bet slip here
                  </p>
                  <p className="text-sm text-muted-foreground">
                    or click to browse
                  </p>
                </div>
                <input
                  type="file"
                  accept="image/*"
                  onChange={handleFileChange}
                  className="hidden"
                  id="file-upload"
                />
                <Button
                  onClick={() => document.getElementById("file-upload")?.click()}
                  variant="outline"
                >
                  Select Image
                </Button>
              </div>
            </div>
          ) : (
            <div className="space-y-4">
              <div className="relative rounded-lg overflow-hidden border bg-muted">
                <img
                  src={selectedImage}
                  alt="Uploaded bet slip"
                  className="w-full h-auto"
                />
              </div>
              <div className="flex gap-3">
                <Button
                  onClick={handleAnalyze}
                  disabled={isAnalyzing}
                  className="flex-1"
                >
                  <ImageIcon className="mr-2 h-4 w-4" />
                  {isAnalyzing ? "Analyzing..." : "Analyze Bet"}
                </Button>
                <Button onClick={handleReset} variant="outline">
                  Reset
                </Button>
              </div>
            </div>
          )}
        </Card>
      </div>
    </div>
  );
}
