import pluginVue from 'eslint-plugin-vue'
import { defineConfigWithVueTs, vueTsConfigs } from '@vue/eslint-config-typescript'


export default defineConfigWithVueTs(
    {
        name: 'app/files-to-lint',
        files: ['**/*.{ts,mts,tsx,vue}'],
    },

    {
        name: 'app/files-to-ignore',
        ignores: ['**/dist/**', '**/dist-ssr/**', '**/coverage/**'],
    },
    {
        name: 'defaultRules',
        rules: {
            'semi': ['error', 'never'],
            'quotes': ['error', 'single'],

            'vue/script-indent': ['error', 'tab', { 'baseIndent': 1 }],
            'comma-dangle': ['error', 'always-multiline'],
            'object-curly-spacing': ['error', 'always'],
            'max-len': ['error', { 'code': 180 }],
            'no-unused-vars': 'off',

            'eqeqeq': ['error', 'always'],
            'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'warn',
            'no-implicit-coercion': 'error',
            'no-else-return': 'error',

            '@typescript-eslint/no-explicit-any': 'error',
            '@typescript-eslint/no-unused-vars': 'error',
            '@typescript-eslint/consistent-type-imports': 'error',
            '@typescript-eslint/no-non-null-assertion': 'error',

            'vue/multi-word-component-names': 'error',
            'vue/no-mutating-props': 'error',
            'vue/require-default-prop': 'error',
            'vue/order-in-components': ['error', {
                order: ['script', 'template', 'style'],
            }],
            'no-await-in-loop': 'error',
        },
    },

    pluginVue.configs['flat/essential'],
    vueTsConfigs.recommended,
)
