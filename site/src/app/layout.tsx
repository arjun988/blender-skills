import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { Navbar } from '@/components/navbar'
import { Footer } from '@/components/footer'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Blender Skills',
  description:
    '94 specialized Blender skills for Cursor, Claude Code, Kiro, and Codex. MCP-first technical art pipelines — modeling, genre/style packs, VFX, and engine export.',
  openGraph: {
    title: 'Blender Skills — 94 Skills for Cursor, Claude Code, Kiro & Codex',
    description:
      '94 specialized Blender skills with 175+ references. Production pipelines via Blender MCP.',
    images: ['/banner.png'],
  },
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  )
}
