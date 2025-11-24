-- ============================================================================
-- Decision-Making Task Management System - SQLite Database Schema
-- ============================================================================
-- This schema defines the database structure for a decision-making task
-- management system that tracks tasks, agents, and audit logs.
--
-- Features:
-- - Three core tables: tasks, agents, audit_log
-- - Foreign key relationships with referential integrity
-- - CHECK constraints for enum validation
-- - Performance indexes on frequently queried columns
-- - JSON columns for flexible metadata storage
-- ============================================================================

-- Enable foreign key constraints (required for SQLite)
PRAGMA foreign_keys = ON;

-- ============================================================================
-- AGENTS TABLE
-- ============================================================================
-- Stores information about agents that can be assigned to tasks.
-- Agents represent entities (human users, AI systems, or services) that
-- perform work on tasks within the system.
-- ============================================================================

CREATE TABLE IF NOT EXISTS agents (
    -- Primary key: Auto-incrementing unique identifier
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    -- Agent name: Must be unique across all agents
    name TEXT NOT NULL UNIQUE,
    
    -- Role type: Categorizes the agent's function in the system
    -- Valid values: 'human', 'ai_assistant', 'service', 'admin'
    role_type TEXT NOT NULL CHECK (role_type IN ('human', 'ai_assistant', 'service', 'admin')),
    
    -- Capabilities: JSON array of agent capabilities/skills
    -- Example: '["task_assignment", "decision_making", "data_analysis"]'
    -- Stored as TEXT for SQLite compatibility
    capabilities_json TEXT,
    
    -- Active status: 1 (active) or 0 (inactive)
    -- Inactive agents cannot be assigned to new tasks
    is_active INTEGER DEFAULT 1 CHECK (is_active IN (0, 1))
);

-- ============================================================================
-- TASKS TABLE
-- ============================================================================
-- Core table storing all tasks in the decision-making system.
-- Each task represents a unit of work that requires decision-making or action.
-- ============================================================================

CREATE TABLE IF NOT EXISTS tasks (
    -- Primary key: Auto-incrementing unique identifier
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    -- Task title: Short descriptive name for the task
    title TEXT NOT NULL,
    
    -- Task description: Detailed explanation of the task requirements
    description TEXT,
    
    -- Task type: Categorizes the task by its nature
    -- Valid values: 'decision', 'review', 'analysis', 'approval', 'implementation'
    task_type TEXT NOT NULL CHECK (task_type IN ('decision', 'review', 'analysis', 'approval', 'implementation')),
    
    -- Options: JSON array of available options/choices for the task
    -- Example: '["option_a", "option_b", "option_c"]'
    -- Stored as TEXT for SQLite compatibility
    options_json TEXT,
    
    -- Assigned agent: Foreign key reference to agents table
    -- NULL if task is unassigned
    -- SET NULL on agent deletion to preserve task history
    assigned_agent_id INTEGER,
    
    -- Task status: Current state of the task
    -- Valid values: 'pending', 'in_progress', 'completed', 'cancelled', 'on_hold'
    status TEXT NOT NULL CHECK (status IN ('pending', 'in_progress', 'completed', 'cancelled', 'on_hold')),
    
    -- Created date: ISO 8601 timestamp when task was created
    -- Format: 'YYYY-MM-DD HH:MM:SS'
    created_date TEXT NOT NULL,
    
    -- Updated date: ISO 8601 timestamp of last task modification
    -- Format: 'YYYY-MM-DD HH:MM:SS'
    updated_date TEXT NOT NULL,
    
    -- Priority: Numeric priority level (1=lowest, 5=highest)
    priority INTEGER CHECK (priority >= 1 AND priority <= 5),
    
    -- Metadata: JSON object for additional task-specific data
    -- Example: '{"tags": ["urgent", "customer"], "deadline": "2024-12-31"}'
    -- Stored as TEXT for SQLite compatibility
    metadata_json TEXT,
    
    -- Foreign key constraint: Ensure assigned agent exists in agents table
    -- ON DELETE SET NULL: Preserve task when agent is deleted
    FOREIGN KEY (assigned_agent_id) REFERENCES agents(id) ON DELETE SET NULL
);

-- ============================================================================
-- AUDIT_LOG TABLE
-- ============================================================================
-- Maintains a complete audit trail of all task state changes.
-- Tracks who made changes, when they were made, and what changed.
-- Critical for compliance, debugging, and historical analysis.
-- ============================================================================

CREATE TABLE IF NOT EXISTS audit_log (
    -- Primary key: Auto-incrementing unique identifier
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    -- Task ID: Reference to the task that was modified
    task_id INTEGER NOT NULL,
    
    -- Action type: Classification of the change that occurred
    -- Valid values: 'created', 'updated', 'assigned', 'status_changed', 'deleted'
    action_type TEXT NOT NULL CHECK (action_type IN ('created', 'updated', 'assigned', 'status_changed', 'deleted')),
    
    -- Previous state: JSON snapshot of task state before change
    -- NULL for 'created' actions
    -- Stored as TEXT for SQLite compatibility
    previous_state TEXT,
    
    -- New state: JSON snapshot of task state after change
    -- Always required to record the resulting state
    new_state TEXT NOT NULL,
    
    -- Changed by: Identifier of the agent/user who made the change
    -- Can be agent name, user ID, or system identifier
    changed_by TEXT NOT NULL,
    
    -- Timestamp: ISO 8601 timestamp when change occurred
    -- Format: 'YYYY-MM-DD HH:MM:SS'
    timestamp TEXT NOT NULL,
    
    -- Notes: Optional human-readable explanation of the change
    -- Useful for context and reasoning behind decisions
    notes TEXT,
    
    -- Foreign key constraint: Ensure audit entries reference valid tasks
    -- ON DELETE CASCADE: Remove audit entries when task is deleted
    FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
);

-- ============================================================================
-- PERFORMANCE INDEXES
-- ============================================================================
-- Indexes on frequently queried columns to optimize read performance.
-- These support common query patterns for filtering and joining.
-- ============================================================================

-- Index on tasks.status: Optimize queries filtering by task status
-- Common query: SELECT * FROM tasks WHERE status = 'pending'
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);

-- Index on tasks.task_type: Optimize queries filtering by task type
-- Common query: SELECT * FROM tasks WHERE task_type = 'decision'
CREATE INDEX IF NOT EXISTS idx_tasks_type ON tasks(task_type);

-- Index on tasks.assigned_agent_id: Optimize queries filtering by assigned agent
-- Common query: SELECT * FROM tasks WHERE assigned_agent_id = ?
-- Also improves JOIN performance with agents table
CREATE INDEX IF NOT EXISTS idx_tasks_assigned_agent ON tasks(assigned_agent_id);

-- Index on audit_log.task_id: Optimize queries retrieving audit history
-- Common query: SELECT * FROM audit_log WHERE task_id = ?
-- Critical for displaying task change history
CREATE INDEX IF NOT EXISTS idx_audit_task_id ON audit_log(task_id);

-- Index on agents.role_type: Optimize queries filtering agents by role
-- Common query: SELECT * FROM agents WHERE role_type = 'human'
CREATE INDEX IF NOT EXISTS idx_agents_role ON agents(role_type);

-- ============================================================================
-- SCHEMA VALIDATION NOTES
-- ============================================================================
-- 1. Foreign Keys: Ensure PRAGMA foreign_keys = ON before using the database
-- 2. JSON Columns: All JSON data stored as TEXT (SQLite native type)
-- 3. Timestamps: Use ISO 8601 format for compatibility and sorting
-- 4. Enum Values: CHECK constraints enforce valid enum values at database level
-- 5. Referential Integrity: Foreign keys maintain data consistency
-- 6. Cascading: audit_log cascades on task deletion, tasks set null on agent deletion
-- ============================================================================
