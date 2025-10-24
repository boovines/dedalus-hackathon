from typing import List, Optional, Dict
from pydantic import BaseModel, Field


class MarketContext(BaseModel):
    title: str = Field(..., description="Market or event title")
    category: str = Field(..., description="High-level category: political, crypto, tech, etc.")
    expiry: Optional[str] = Field(None, description="ISO date for resolution, if known")


class Factor(BaseModel):
    name: str = Field(..., description="Key factor to investigate")
    description: str = Field(..., description="Why this factor matters for the outcome")


class ResearchTask(BaseModel):
    source: str = Field(..., description="Logical source key, e.g., twitter, reddit")
    objectives: List[str] = Field(..., description="What to find out using this source")
    search_terms: List[str] = Field(default_factory=list, description="Helpful queries or entities")


class SourceFinding(BaseModel):
    source: str = Field(..., description="Logical source key, e.g., twitter, reddit")
    summary: str = Field(..., description="Condensed evidence and reasoning from this source")
    probability: Optional[float] = Field(None, description="Source-implied probability [0,1]")
    confidence: Optional[float] = Field(None, description="Model confidence in this source [0,1]")
    citations: List[str] = Field(default_factory=list, description="Relevant links or references")
    factor: Optional[str] = Field(None, description="Which factor this evidence primarily addresses")


class OrchestrationResult(BaseModel):
    context: MarketContext
    selected_servers: Dict[str, str] = Field(..., description="Mapping of source key -> MCP server slug")
    factors: List[Factor] = Field(default_factory=list)
    tasks: List[ResearchTask] = Field(default_factory=list)
    findings: List[SourceFinding]
    final_probability: float = Field(..., description="Aggregated probability [0,1]")
    confidence: float = Field(..., description="Overall confidence [0,1]")
