# Contract Redline Analysis and Recommendation Skill

This skill ingests contract redlines, assesses proposed changes against the
company's commercial practice guidelines (or Commercial Practice Guide, if
provided by the user), and recommends negotiation actions (`[ACCEPT]`,
`[REJECT]`, `[COUNTER]`) tailored to commercial risk tolerance.

## Source Details

This skill was derived from the following Gemini Gem and reference
documentation:

-   **Source Gem (Corp)**:
    [Contract Redline Analysis and Recommendation](https://gemini.google.com/corp/gem/a15ff666f5f3?resourcekey=0-_HntrtOe8UAoH9FR14QzAw&usp=sharing)
-   **Source Gem (Public)**:
    [Contract Redline Analysis and Recommendation](https://gemini.google.com/gem/1JdZo49PwEGDcfGiE7JyIWpZzY-n27GZ0?resourcekey=0-mSfDTuyMIbDMkGViaU6t4g&usp=sharing)
-   **Source Documentation**:
    [Legal AI Agent Reference](https://docs.google.com/document/d/1xjNVti2c6qvELrfYf1DBp30AN0uVXf2sdB0wU57BT-o/edit?tab=t.cmlpiwlqtmo5#heading=h.yrtcasxk0npj)
-   **Source Drive (Canonical)**:
    [Google Drive Gem Spec](https://drive.google.com/file/d/1f67-KmBdkmDXnkJFp2ZJPJQkd47rUPGn/view)
    ([Alt Drive Link](https://drive.google.com/file/d/1JdZo49PwEGDcfGiE7JyIWpZzY-n27GZ0/view))
-   **Tracking Bug**: [b/572085439](http://b/572085439)

## Repository Structure

-   **`template.jinja2.md`**: Modular Jinja2 template supporting both ADK
    (in-memory document retrieval via LERA tool ecosystem) and script/harness
    environments.
-   **Compiled Target (ADK)**:
    `research/infra/externalization/api_backend/partners/legal_ai/lera/agent/adk/skills/contract-redline-analysis-and-recommendation/SKILL.md`
-   **Compiled Target (Script)**:
    `research/infra/externalization/api_backend/partners/legal_ai/lera/agent/skills/contract-redline-analysis-and-recommendation/SKILL.md`
