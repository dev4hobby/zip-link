import type { NextPage } from 'next'
import Head from 'next/head'
import { Box, Button, Divider, Modal, Typography } from '@mui/material';
import styles from '../styles/Home.module.css'
import { useRef, useState } from 'react'
import { apiBaseUrl } from '../env';
import TextField from '@mui/material/TextField';
import LineWeight from '@mui/icons-material/LineWeight';
import ExitToAppIcon from '@mui/icons-material/ExitToApp';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import ShareIcon from '@mui/icons-material/Share';
import { CopyToClipboard } from 'react-copy-to-clipboard';


const Home: NextPage = () => {
  const [open, setOpen] = useState(false);
  const [url, setUrl] = useState('');
  const [copied, setCopied] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  const inputRef = useRef<HTMLInputElement>(null)

  const getUrlAndZip = async (e: any) => {
    e.preventDefault()
    if (!inputRef.current) {
      return
    }
    const url = inputRef.current.value
    const response = await fetch(`${apiBaseUrl}/url`, {
      method: 'POST',
      body: JSON.stringify({ 'url': url }),
    }).then(res => res.json())
    console.log(response)
    setUrl(response.url)
    handleOpen()
  }

  const shareUrl = (url: string) => {
    if (navigator.share) {
      navigator.share({
        title: 'Z1pLink',
        text: 'Make your links short and easy to share',
        url: url
      })
    } else {
      window.alert("Only works on Mobile browsers")
    }
  }

  const handleCopy = () => {
    setCopied(true)
    window.alert("Copied to clipboard")
    setTimeout(() => {
      setCopied(false)
    }, 1000)
  }

  const openInNewTab = (url:string) => {
    if (!url) {
      return
    }
    if (!open) {
      return
    }
    window.open(url, '_blank', 'noopener,noreferrer');
  };

  return (
    <>
    <div className={styles.navigation}>
      <div className={styles.navTitle}>
        ZipLink
      </div>
    </div>
    <div className={styles.container}>
      <Head>
        <title>Z1pLink</title>
        <meta property="og:title" content="Z1pLink" />
        <meta property="og:image" content="https://z1plink.com/public/zip_link.png" />
        <meta property="og:description" content="Make your links short and easy to share" />
        <meta property="og:image:width" content="1200" />
        <meta property="og:image:height" content="630" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        Make short your link and share it with your friends
        <Divider style={{width:'100%', marginTop:'1.8em', marginBottom: '1.8em'}} />
        <div className={styles.inputGroup} style={{width:'98%'}}>
          <TextField fullWidth inputRef={inputRef} name="url" id="url" label="URL" variant="standard"/>
          <Button variant="outlined" size="large" onClick={getUrlAndZip}>
            ZIP&nbsp;<LineWeight></LineWeight>
          </Button>
          <Modal open={open} onClose={handleClose} aria-labelledby="modal-modal-title" aria-describedby="modal-modal-description">
            <Box sx={{position: 'absolute' as 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', width: 400, bgcolor: 'background.paper', border: '2px solid #000', boxShadow: 24, p: 4}}>
              <Typography id="modal-modal-title" variant="h6" component="h2">
                Your Z1p-link ready !
              </Typography>
              <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                <div style={{display: 'flex', justifyContent: 'space-between'}}>
                  {url}
                  <div onClick={() => openInNewTab(url)}><ExitToAppIcon></ExitToAppIcon></div>
                  <CopyToClipboard text={url} onCopy={() => handleCopy()}>
                    <ContentCopyIcon></ContentCopyIcon>
                  </CopyToClipboard>
                  <ShareIcon onClick={() => shareUrl(url)}></ShareIcon>
                </div>
              </Typography>
            </Box>
          </Modal>
        </div>
      </main>
      <footer className={styles.footer}>
        D3fau1t: ZipLink
      </footer>
    </div>
    </>
  )
}

export default Home