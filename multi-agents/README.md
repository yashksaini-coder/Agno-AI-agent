# Agno Agent Tool

A demonstration of the Agno Agent framework for building AI assistants with integrated tool calling capabilities.

## Overview

The Agno Agent is a versatile tool that performs various tasks including information search, text generation, and summarization. This repository showcases how to implement and use the Agno Agent with proper tool call parameters.

## Features

- **Flexible Tool Calling**: Define and execute tool calls with custom parameters
- **Multiple Functions**: Search for information, generate text, summarize content
- **Parameter Validation**: Strong typing support for tool parameters
- **Easy Integration**: Simple API for integrating with your applications

## Tool Call Parameters

| Parameter | Description | Type | Example |
|-----------|-------------|------|---------|
| `tool_name` | Name of the tool | string | "Agno Agent" |
| `tool_description` | Description of the tool's functionality | string | "A tool for various tasks like searching, generating text, etc." |
| `tool_parameters` | List of available tool parameters | array | ["search", "generate", "summarize"] |
| `tool_parameter_descriptions` | Descriptions for each parameter | array | ["Search for information", "Generate text", "Summarize text"] |
| `tool_parameter_types` | Data types for parameters | array | ["string", "string", "string"] |
| `tool_parameter_examples` | Usage examples | array | ["What is the capital of France?", "Write a poem about the sea.", "Summarize the following text: ..."] |

## Demo

Here are some examples of the Agno Agent in action:

![Demo 1](./public/demo-1.png)
![Demo 2](./public/demo-2.png)
![Demo 3](./public/demo-3.png)

## Documentation

For more detailed information, please refer to:

- [Agno Documentation](https://docs.agno.ai)
- [Tool Calling Guide](https://docs.agno.ai/guide/tool-calling)
- [API Reference](https://docs.agno.ai/api)

---

<a href="https://github.com/yashksaini-coder">
    <table>
        <tbody>
            <tr>
                <td align="left" valign="top" width="14.28%">
                    <img src="https://github.com/yashksaini-coder.png?s=60" width="130px;"/>
                    <br/>
                    <h4 align="center">
                        <b>Yash K. Saini</b>
                    </h4>
                    <div align="center">
                        <p>(Author)</p>
                    </div>
                </td>
                <td align="left" valign="top" width="85%">
                    <p>
                        👋 Hi there! I'm <u><em><strong>Yash K. Saini</strong></em></u>, a self-taught software developer and a computer science student from India.
                    </p>
                    <ul>
                     <li>
                        I love building & contributing to Open Source software solutions & projects that help solve real-world problems.
                    </li>
                    <li>
                        I want to build products & systems that can benefit & solve problems for many other DEVs.
                    </li>
                </td>
            </tr>
        </tbody>
    </table>
</a>

<p align="center">
    <strong>🌟 If you find this project helpful, please give it a star on GitHub! 🌟</strong>
</p>