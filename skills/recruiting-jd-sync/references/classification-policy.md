# Classification And Resume Mapping

Classify from the collected JD text. Do not assume a fixed category set unless the project already defines one.

## Category State

### Initialization State

Use when no stable resume variants exist yet.

- Cluster jobs by technical requirements.
- Default to three categories if the evidence is not enough for a more precise split.
- Assign `D1`, `D2`, `D3` IDs.
- Mark resume mapping as pending.

Typical default clusters:

- applied AI / Agent / RAG / workflow / product engineering,
- classic algorithms / CV / ML / domain algorithms,
- LLM / multimodal / training / evaluation / infrastructure.

### Transitional State

Use when job categories exceed available resume variants.

- Preserve category accuracy.
- Use resume placeholders for categories without finished resumes.
- Do not merge categories merely to match resume count unless the user asks.
- Make placeholder names explicit, such as `D4_resume_pending` or `04_后训练RL_评测Infra（待导出）`.

### Complete State

Use when category count and usable resume variants align.

- Map each category to a specific PDF or resume file.
- Write actual resume filenames in the workbook's recommendation column.
- Keep placeholder values only for explicitly unfinished variants.

## ID Policy

Use inventory IDs in the form:

```text
D{category}-{sequence}
```

Examples: `D1-01`, `D2-14`, `D4-20`.

Rules:

- The ID is the only formal cross-file key.
- Sequence numbers are category-local.
- Keep existing IDs stable when adding new roles.
- Do not renumber existing IDs unless the user explicitly requests a classification migration.
- If a category is renamed but still maps to the same set, keep the `D` number stable.

## Technical Signals

Use these signals to classify, adapting names to the project:

- Agent/RAG/application engineering: Agent, RAG, Tool Use, Function Calling, workflow, memory, prompt/context engineering, AI tooling, productized LLM applications.
- Classic algorithms/CV/ML: computer vision, detection, segmentation, ReID, recommendation, search/ranking, robotics, haptics, medical imaging, PyTorch/TensorFlow model training without LLM as the main center.
- LLM/multimodal/application algorithms: LLM, VLM, multimodal understanding, video/image/text generation, model deployment, inference service, fine-tuning as part of application algorithms.
- Post-training/RL/eval/infra: SFT, RLHF, DPO, PPO, GRPO, RLVR, reward model, benchmark/evaluation, distributed training, inference acceleration, AI infrastructure.
- Low-depth/product/data roles: AI product, data annotation, model evaluation operations, prompt templates, workflow support. Keep them if useful, but mark lower application priority.

## Workbook Recommendation Rule

The workbook recommendation column should reflect the current mapping state:

- complete: actual resume PDF/file name,
- transitional: explicit pending placeholder,
- initialization: category label or `resume_pending`.

Avoid writing a resume file that does not exist.
