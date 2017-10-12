package com.intellij.plugin.embersnippets;

import com.intellij.codeInsight.template.impl.DefaultLiveTemplatesProvider;
import org.jetbrains.annotations.Nullable;

public class EmberSnippetsTemplatesProvider implements DefaultLiveTemplatesProvider {

    @Override
    public String[] getDefaultLiveTemplateFiles() {
        return new String[]{
            "liveTemplates/import-application",
            "liveTemplates/import-array",
            "liveTemplates/import-base",
            "liveTemplates/import-component",
            "liveTemplates/import-controller",
            "liveTemplates/import-debug",
            "liveTemplates/import-engine",
            "liveTemplates/import-map",
            "liveTemplates/import-object",
            "liveTemplates/import-polyfills",
            "liveTemplates/import-routing",
            "liveTemplates/import-rsvp",
            "liveTemplates/import-runloop",
            "liveTemplates/import-service",
            "liveTemplates/import-string",
            "liveTemplates/import-test",
            "liveTemplates/import-utils"
        };
    }

    @Nullable
    @Override
    public String[] getHiddenLiveTemplateFiles() {
        return null;
    }
}
